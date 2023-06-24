import datetime
import os
import shutil

import pytube
import pywhisper
import yt_dlp
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
    clip.audio.write_audiofile(filename[:-5] + ".mp3")
    clip.close()


def main(link, model):
    print('Convert Youtube videos to mp3 files and then transcribe them to text using Whisper.')
    print("URL: " + link)
    print("MODEL: " + model)
    print("Downloading video... Please wait.")

    try:
        filename = download_video(pytube.YouTube(link).watch_url)
        print("Downloaded video as " + filename)
    except:
        print("Not a valid link...")
        return

    try:
        convert_to_mp3(filename)
        print("Converted video to mp3")
    except:
        print("Error converting video to mp3")
        return

    try:
        mymodel = pywhisper.load_model(model)
        result = mymodel.transcribe(filename[:-5] + ".mp3")

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
        return data
    except Exception as e:
        print("Error transcribing audio to text")
        print(e)
        return


if __name__ == "__main__":
    main()
