import random
from datetime import datetime, date
import os

class Utils:
    
    def __init__(self, channel=None, url=None, error_list=None, historic_list=None, item_name=None) -> None:
        self.channel       = channel
        self.url           = url
        self.error_list    = error_list
        self.historic_list = historic_list
        self.item_name     = item_name

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
                print(f'O arquivo {file} não possui até 40 urls.')
        if url_list:
            return url_list
        else:
            return False        

    def create_video_folder(self):
        path = f'channels/{self.channel}/Videos/Video_{self.url}_{datetime.now().strftime("%m-%d-%Y")}_{datetime.now().strftime("%H-%M-%S")}'
        os.mkdir(path)
        return path
    
    def update_error_file(self):
        error_file = open(f'channels/{self.channel}/Arquivos/error/error_{self.item_name}.txt', 'r', encoding='utf-8')

        print(f'Arquivo error_{self.item_name}.txt atualizado com sucesso.')
        pass

    def update_historic_file(self):
        print(f'Arquivo historic_{self.item_name}.txt atualizado com sucesso.')
        pass


