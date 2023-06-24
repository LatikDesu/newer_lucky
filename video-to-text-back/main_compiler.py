import datetime
import os

import pytube
import pywhisper
import static_ffmpeg
import yt_dlp
from moviepy.editor import VideoFileClip

from paragraphs_generator import paragraphs_generator
from screenshots_generator import screenshots_generator
from timecode_generator import timecode_generator


def format_timedelta(td):
    """Служебная функция для классного форматирования объектов timedelta (например, 00:00:20.05)
    исключая микросекунды и сохраняя миллисекунды"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00"
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:00}"


def download_video_dlp(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        downloaded_file_path = ydl.prepare_filename(info_dict)
    print(
        f"Видео {downloaded_file_path} успешно загружено!")

    return downloaded_file_path


def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-5] + ".mp3")
    clip.close()


def audio_to_text(filename):
    model = pywhisper.load_model("base")
    result = model.transcribe(filename)
    print(result["text"])
    sonic = result["text"]
    return sonic


def main(link, model):
    print('''
    This tool will convert Youtube videos to mp3 files and then transcribe them to text using Whisper.
    ''')
    print("URL: " + link)
    print("MODEL: " + model)
    # FFMPEG installed on first use.
    print("Initializing FFMPEG...")
    static_ffmpeg.add_paths()

    print("Downloading video... Please wait.")
    try:
        filename = download_video_dlp(pytube.YouTube(link).watch_url)
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

        paragraphs = paragraphs_generator(result["text"])

        timecodes = timecode_generator(paragraphs, result['segments'])

        screenshots = screenshots_generator(filename, timecodes)

        data = {}

        for items in timecodes:
            data.update({
                items: {
                    "title": filename[:-5],
                    "start": format_timedelta(datetime.timedelta(seconds=timecodes[items]['start'])),
                    "end": format_timedelta(datetime.timedelta(seconds=timecodes[items]['end'])),
                    "text": paragraphs[int(items)],
                    "screenshot": screenshots[items]
                },
            })

        os.remove(filename)
        os.remove(filename[:-5] + ".mp3")

        print("Removed video and audio files")
        print("Done!")
        return data
    except Exception as e:
        print("Error transcribing audio to text")
        print(e)
        return


if __name__ == "__main__":
    main()
