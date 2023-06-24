import os

from moviepy.video.io.VideoFileClip import VideoFileClip


def get_video_meta(filename):
    metadata = {
        "title": None,
        "duration": None,
        "fps": None,
        "size": None,
        "rotation": None
    }

    try:
        clip = VideoFileClip(filename)

        metadata = {
            "title": os.path.splitext(os.path.basename(clip.filename))[0],
            "duration": clip.duration,
            "fps": clip.fps,
            "size": clip.size,
            "rotation": clip.rotation
        }
        clip.close()

        return metadata

    except:
        return metadata
