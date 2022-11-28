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
                lines = random.sample(lines, 40)
                url_dict = {file:lines}
                url_list.append(url_dict)
            except:
                print(f'O arquivo {file}.txt não possui até 40 urls.')
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

    def generate_title_description_hashtag(self):
        hashtag_combo_1 = self.generate_hashtag_combo()
        hashtag_combo_2 = self.generate_hashtag_combo()

        title = open(f'channels/{self.channel}/Arquivos/titles/{self.item_name}_title.txt', 'r', encoding='utf-8').readlines()[0]
        file = open(f'channels/{self.channel}/Arquivos/utils/base_description.txt', 'r', encoding='utf-8')
        data = file.read()
        data = data.replace('Título', title).replace('Hashtags_1', hashtag_combo_1).replace('Hashtags_2', hashtag_combo_2)
        file.close()

        file = open(f'channels/{self.channel}/Videos/{self.series_folder}/Video_{self.item_name}/title_description_hashtag.txt', 'w', encoding='utf-8')
        file.write(data)
        file.close()
        return None


    def generate_hashtag_combo(self):
        file = open(f'channels/{self.channel}/Arquivos/keywords/{self.item_name}_keywords.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        lines = random.sample(lines, 45)
        hashtag_combo = ''
        for line in lines:
            line = line.replace('#', '')
            line = line.split()[0]
            hashtag_combo = hashtag_combo + line + ','
        hashtag_combo = hashtag_combo[:-1]
        return hashtag_combo


# if __name__ == '__main__':
#     Utils(item_name='asmr',channel='Dopaminando', series_folder='Video_Series_11-21-2022_21-54-41').generate_title_description_hashtag()
