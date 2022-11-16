from instagrapi import Client

cl = Client()
cl.login(username='ldolenc902', password='Dolenc123@')

class Instagram:

    def __init__(self, url, path) -> None:
        self.url = url
        self.path = path
    
    def download_video(self):
        try:
            media_pk =cl.media_pk_from_url(self.url)
            cl.clip_download(media_pk=media_pk, folder=f'{self.path}/')
            return False
        except:
            print(f'Falha ao baixar vídeo: {self.url}')
            return self.url