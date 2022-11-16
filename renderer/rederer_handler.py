from moviepy.editor import *
from utils import Utils

IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe")

class RendererHandler:

    def __init__(self, channel, series_folder) -> None:
        self.channel        = channel
        self.series_folder  = series_folder

    def handler(self):
        folders = os.listdir(f'channels/{self.channel}/Videos/{self.series_folder}/')
        for folder in folders:
            background = Utils(channel=self.channel).get_random_background()
            video_list = os.listdir(f'channels/{self.channel}/Videos/{self.series_folder}/{folder}')
            video_list = [video for video in video_list if '.mp4' in video]
            for video in video_list:
                clip = VideoFileClip(f'channels/{self.channel}/Videos/{self.series_folder}/{folder}/{video}').resize(height=1080)
                duration = clip.duration
                background_image = ImageClip(f'channels/{self.channel}/Backgrounds/{background}' + '.jpg').set_duration(duration)   
                composition = CompositeVideoClip([background_image, clip.set_position("center")])
                video = video[:-4]
                composition.write_videofile(f'channels/{self.channel}/Videos/{self.series_folder}/{folder}/{video}_new' + '.mp4')
        return None

