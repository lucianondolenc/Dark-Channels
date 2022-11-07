import json
from downloader.downloader_handler import DownloaderHandler


def main():
    channels = json.load(open('channels.json'))
    for channel in channels:
        pass


if __name__ == '__main__':
    main()