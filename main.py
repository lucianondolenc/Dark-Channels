import json
from downloader.downloader_handler import DownloaderHandler
from renderer.rederer_handler import RendererHandler


def main():
    channels = json.load(open('channels.json'))
    for channel in channels:
        response = DownloaderHandler(channel=channel['nome_canal']).handler()
        response = RendererHandler(channel=channel['nome_canal'], series_folder=response['series_folder']).handler()


if __name__ == '__main__':
    main()