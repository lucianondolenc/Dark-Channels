import random
from datetime import datetime, date
import os
import re

class Utils:
    
    def __init__(self, channel=None, url=None, url_list=None, item_name=None, series_folder=None, file_path=None) -> None:
        self.channel       = channel
        self.url           = url
        self.url_list      = url_list
        self.item_name     = item_name
        self.series_folder = series_folder
        self.file_path     = file_path

    def get_url_list(self):
        files = os.listdir(f'channels/{self.channel}/Arquivos/urls/')
        files = [file.replace('.txt', '') for file in files]
        url_list = []
        for file in files:
            try:
                url_file = open(f'channels/{self.channel}/Arquivos/urls/{file}.txt', 'r', encoding='utf-8')
                lines = url_file.readlines()
                lines = [line.strip() for line in lines if len(line) > 5]
                lines = list(dict.fromkeys(lines))
                lines = random.sample(lines, 8)
                url_dict = {file:lines}
                url_list.append(url_dict)
            except:
                print(f'O arquivo {file} não possui até 40 urls.')
        if url_list:
            return url_list
        else:
            return False

    def create_video_series_folder(self):
        series_folder = f'Video_Series_{datetime.now().strftime("%m-%d-%Y")}_{datetime.now().strftime("%H-%M-%S")}'
        series_path = f'channels/{self.channel}/Videos/{series_folder}'
        os.mkdir(series_path)
        return series_folder        

    def create_video_folder(self):
        path = f'channels/{self.channel}/Videos/{self.series_folder}/Video_{self.url}'
        os.mkdir(path)
        return path

    def update_file(self):
        # read the file
        if 'urls' in self.file_path:
            file = open(f'{self.file_path}', 'r', encoding='utf-8')
            lines = file.readlines()
            lines = [line.strip() for line in lines if len(line) > 5]
            lines = list(set(lines) - set(self.url_list))
            lines = list(dict.fromkeys(lines))
            file.close()
        else:
            file = open(f'{self.file_path}', 'r', encoding='utf-8')
            lines = file.readlines()
            lines = [line.strip() for line in lines if len(line) > 5]
            lines = lines + self.url_list
            lines = list(dict.fromkeys(lines))
            file.close()

        # write into the file
        file = open(f'{self.file_path}', 'w', encoding='utf-8')
        for url in lines:
            file.write(url+'\n')
        file.close()

        return None

    def get_random_background(self):
        backgrounds_list = os.listdir(f'channels/{self.channel}/Backgrounds/')
        backgrounds_list = [item[:-4] for item in backgrounds_list if item[-4:] == '.jpg']
        background = random.sample(backgrounds_list, 1)[0]
        return background



# if __name__ == '__main__':
#     Utils(channel='Dopaminando').get_random_background()