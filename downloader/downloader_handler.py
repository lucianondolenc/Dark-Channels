from utils import Utils
import time
from downloader.instagram import Instagram

class DownloaderHandler:
    
    def __init__(self, channel) -> None:
        self.channel = channel

    def handler(self):
        url_list = Utils(channel=self.channel).get_url_list()
        series_folder = Utils(channel=self.channel).create_video_series_folder()
        response = {'series_folder':series_folder, 'information':[]}
        information_list = []
        if url_list:
            for item in url_list:
                item_name = list(item.keys())[0]
                path = Utils(channel=self.channel, url=item_name, series_folder=series_folder).create_video_folder()
                historic_list = []
                error_list = []
                for url in item[item_name]:       
                    if 'instagram' in url:
                        response = Instagram(url=url,path=path).download_video()
                        if not response:
                            historic_list.append(url)
                        else:
                            error_list.append(url)
                    elif 'tiktok' in url:
                        pass
                information_dict = {'item_name':item_name, 'historic_list': historic_list, 'error_list':error_list}
                information_list.append(information_dict)
        response = {'series_folder':series_folder, 'information':information_list}
        return response
                 
                
