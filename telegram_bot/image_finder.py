from Restobot.config import config
from requests import request

def image_finder(url:str):
    print('looking for picture url:', url)

    if not url:
        return config.no_picture_url

    path = config.img_folder_url + str(url)
    response = request('GET', path)
    if response.status_code != 200:
        print ('picture not found')
        return config.no_picture_url

    print ('picture found:', path)
    return path


