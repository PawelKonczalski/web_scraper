from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def start_search():
    search = input('Search for: ')
    search = search.replace(' ', '+')
    params = {'q': search}

    dir_name = search.replace(' ', '_')

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get('https://www.bing.com/images/search', params)

    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.findAll('a', {'class': 'thumb'})

    for item in links:
        img_obj = requests.get(item.attrs['href'])
        print('Getting:', item.attrs['href'])
        title = item.attrs['href'].split('/')[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save('./' + dir_name + '/' + title, img.format)
        except:
            print('Could not save image.')


start_search()
