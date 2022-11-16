import json
from downloader.downloader_handler import DownloaderHandler


def main():
    channels = json.load(open('channels.json'))
    for channel in channels:
        series_folder = DownloaderHandler(channel=channel['nome_canal']).handler()


if __name__ == '__main__':
    main()