import random
from datetime import datetime, date
import os

class Utils:
    
    def __init__(self, channel) -> None:
        self.channel = channel

    def get_url_list(self):
        try:
            url_file = open(f'channels/{self.channel}/Arquivos/urls.txt', 'r', encoding='utf-8')
            lines = url_file.readlines()
            lines = [line.strip() for line in lines if len(line) > 5]
            lines = list(dict.fromkeys(lines))
            lines = random.sample(lines, 40)
            return lines
        except:
            return False

    def create_video_folder(self):
        path = f'channels/{self.channel}/Videos/Video_{datetime.now().date()}'
        os.mkdir(path)
        return path

