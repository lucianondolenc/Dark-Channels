from utils import Utils

class DownloaderHandler:
    
    def __init__(self, channel) -> None:
        self.channel = channel

    def handler(self):
        url_list = Utils(channel=self.channel).get_url_list()
        if url_list != False:
            response = Utils(channel=self.channel).create_video_folder()
            for url in url_list:        
                if "instagram" in url:
                    pass

                elif "tiktok" in url:
                    pass
