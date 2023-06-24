import math

import nltk
import numpy as np
from scipy.signal import argrelextrema
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def rev_sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(0.5 * x))


def activate_similarities(similarities: np.array, p_size=10) -> np.array:
    x = np.linspace(-10, 10, p_size)
    y = np.vectorize(rev_sigmoid)
    activation_weights = np.pad(y(x), (0, similarities.shape[0] - p_size))
    diagonals = [similarities.diagonal(each) for each in range(0, similarities.shape[0])]
    diagonals = [np.pad(each, (0, similarities.shape[0] - len(each))) for each in diagonals]
    diagonals = np.stack(diagonals)
    diagonals = diagonals * activation_weights.reshape(-1, 1)
    activated_similarities = np.sum(diagonals, axis=0)
    return activated_similarities


def paragraphs_generator(result: str):
    sentences = nltk.sent_tokenize(result)
    print(f'Loaded Text String ({len(sentences)} sentences)')

    model = SentenceTransformer('all-mpnet-base-v2')

    sentence_length = [len(each) for each in sentences]
    long = np.mean(sentence_length) + np.std(sentence_length) * 2
    short = np.mean(sentence_length) - np.std(sentence_length) * 2

    text = ''
    for each in sentences:
        if len(each) > long:
            comma_splitted = each.replace(',', '.')
        else:
            text += f'{each}. '
    sentences = text.split('. ')

    text = ''
    for each in sentences:
        if len(each) < short:
            text += f'{each} '
        else:
            text += f'{each}. '

    sentences = text.split('. ')
    embeddings = model.encode(sentences)

    print(embeddings.shape)

    similarities = cosine_similarity(embeddings)

    activated_similarities = activate_similarities(similarities, p_size=embeddings.shape[0])

    minmimas = argrelextrema(activated_similarities, np.less, order=2)

    split_points = [each for each in minmimas[0]]
    result = []
    text = ''
    for num, each in enumerate(sentences):
        if num in split_points:
            result.append(text)
            text = f' {each} '
        else:
            text += f' {each} '

    result.append(text)
    return result