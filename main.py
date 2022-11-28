import json
from downloader.downloader_handler import DownloaderHandler
from renderer.rederer_handler import RendererHandler
from utils import Utils


def main():
    channels = json.load(open('channels.json'))
    for channel in channels:
        response_downloader = DownloaderHandler(channel=channel['nome_canal']).handler()
        response_renderer = RendererHandler(channel=channel['nome_canal'], series_folder=response_downloader['series_folder']).handler()

        for item in response_downloader['information']:

            # Update Files
            Utils(item_name=item['item_name'], url_list=item['error_list'], file_path=f'channels/{channel["nome_canal"]}/Arquivos/error/error_{item["item_name"]}.txt').update_file()
            Utils(item_name=item['item_name'], url_list=item['historic_list'], file_path=f'channels/{channel["nome_canal"]}/Arquivos/historic/historic_{item["item_name"]}.txt').update_file()
            Utils(item_name=item['item_name'], url_list=item['historic_list'], file_path=f'channels/{channel["nome_canal"]}/Arquivos/urls/{item["item_name"]}.txt').update_file()

            # Create title, description and hashtags
            Utils(item_name=item['item_name'], chanel=channel['nome_canal'],series_folder=response_downloader['series_folder']).generate_title_description_hashtag()

if __name__ == '__main__':
    main()