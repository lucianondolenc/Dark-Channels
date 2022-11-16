import random
from datetime import datetime, date
import os

class Utils:
    
    def __init__(self, channel=None, url=None, url_list=None, item_name=None, file_path=None) -> None:
        self.channel       = channel
        self.url           = url
        self.url_list      = url_list
        self.item_name     = item_name
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

    def create_video_folder(self):
        path = f'channels/{self.channel}/Videos/Video_{self.url}_{datetime.now().strftime("%m-%d-%Y")}_{datetime.now().strftime("%H-%M-%S")}'
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
        

# if __name__ == '__main__':
#     Utils(item_name='asmr', url_list=['https://www.instagram.com/reel/Ciu75XjA4vh/?igshid=NzNkNDdiOGI=', 'https://www.instagram.com/reel/CjGgNCuJSv7/?igshid=NzNkNDdiOGI='], file_path='channels/Dopaminando/Arquivos/urls/asmr.txt').update_file()