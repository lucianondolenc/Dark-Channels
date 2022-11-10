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
                        response = None
                        if not response:
                            error_list.append(url)
                        else:
                            historic_list.append(url)
                    elif 'tiktok' in url:
                        pass
                Utils(item_name=item_name, error_list=error_list).update_error_file()
                Utils(item_name=item_name,historic_list=historic_list).update_historic_file()  
                
