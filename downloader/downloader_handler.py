from utils import Utils

class DownloaderHandler:
    
    def __init__(self, channel) -> None:
        self.channel = channel

    def handler(self):
        url_list = Utils(channel=self.channel).get_url_list()
        print(url_list)
