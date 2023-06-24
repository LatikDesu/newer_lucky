import os
import urllib.parse

from moviepy.video.io.VideoFileClip import VideoFileClip


def screenshots_generator(link, timecode):
    try:
        clip = VideoFileClip(link)

        # filename, _ = os.path.splitext(link[:-4])
        # filename += "-screenshots"
        # path = os.path.join("static", filename)
        # if not os.path.isdir(path):
        #     os.mkdir(path)

        screenshots_dict = {}

        for record in timecode:
            frame_filename = os.path.join("static", f"frame{timecode[record]['start']}.png")
            normal = os.path.join(f"frame{timecode[record]['start']}.png")
            new_path = os.path.normpath(urllib.parse.unquote(normal))

            clip.save_frame(frame_filename, timecode[record]['start']+1)
            screenshots_dict.update({
                record: new_path
            })
        clip.close()
        return screenshots_dict

    except Exception as e:
        print("Cannot take screenshot")
        print(e)
        return
