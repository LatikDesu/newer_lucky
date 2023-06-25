import datetime
import os
import shutil

import pytube
import pywhisper
import yt_dlp
from loguru import logger
from moviepy.editor import VideoFileClip

from processing_features.processing_meta import get_video_meta
from processing_features.processing_paragraphs import get_text_paragraphs
from processing_features.processing_timecodes import get_text_timecodes


def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best',
        'outtmpl': 'download_video/%(title)s/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        downloaded_file_path = ydl.prepare_filename(info_dict)

    return downloaded_file_path


def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename.split('.')[0] + ".mp3")
    clip.close()


def main(link, model):
    print('Convert Youtube videos to mp3 files and then transcribe them to text using Whisper.')
    print("URL: " + link)
    print("MODEL: " + model)
    print("Downloading video... Please wait.")

    logger.info(f"Запуск...")
    logger.info("URL: " + link)
    logger.info("MODEL: " + model)
    logger.info(f"Загрузка видео...")

    try:
        filename = download_video(pytube.YouTube(link).watch_url)
        print("Downloaded video as " + filename)
    except:
        print("Not a valid link...")
        logger.info("Ошибка ссылки...")
        return

    try:
        convert_to_mp3(filename)
        print("Converted video to mp3")
        logger.info("Конвертация видео в mp3")
    except:
        print("Error converting video to mp3")
        logger.info("Ошибка конвертации видео в mp3...")
        return

    try:
        mymodel = pywhisper.load_model(model)
        result = mymodel.transcribe(filename.split('.')[0] + ".mp3")

        metadata = get_video_meta(filename)
        text_paragraphs, text_sentences = get_text_paragraphs(result["text"])
        pwt, swt = get_text_timecodes(text_paragraphs, text_sentences, result['segments'])

        data = dict()
        data["metadata"] = metadata
        data["paragraphs"] = text_paragraphs
        data["sentences"] = text_sentences

        video_path = os.path.basename(os.path.dirname(os.path.abspath(filename)))
        shutil.rmtree('download_video/' + video_path)

        print("Removed video and audio files")
        print("Done!")
        logger.info("Удаляем видео и аудио файлы...")
        logger.info("Готово!")
        return data
    except Exception as e:
        print("Error transcribing audio to text")
        logger.info("Ошибка преобразования аудио в текст...")
        print(e)
        return


if __name__ == "__main__":
    main()
