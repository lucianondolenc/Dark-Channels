from utils import Utils
import time
from downloader.instagram import Instagram

class DownloaderHandler:
    
    def __init__(self, channel) -> None:
        self.channel = channel

    def handler(self):
        url_list = Utils(channel=self.channel).get_url_list()
        if url_list:
            for item in url_list:
                item_name = list(item.keys())[0]
                path = Utils(channel=self.channel, url=item_name).create_video_folder()
                historic_list = []
                error_list = []
                for url in item[item_name]:       
                    if 'instagram' in url:
                        response = Instagram(url=url,path=path).download_video()
                        if not response:
                            error_list.append(url)
                        else:
                            historic_list.append(url)
                    elif 'tiktok' in url:
                        pass
                Utils(item_name=item_name, url_list=error_list, file_path=f'channels/{self.channel}/Arquivos/error/error_{item_name}.txt').update_file()
                Utils(item_name=item_name, url_list=historic_list, file_path=f'channels/{self.channel}/Arquivos/historic/historic_{item_name}.txt').update_file()
                Utils(item_name=item_name, url_list=historic_list, file_path=f'channels/{self.channel}/Arquivos/urls/{item_name}.txt').update_file()
                 
                
