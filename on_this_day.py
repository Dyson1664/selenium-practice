import requests
from bs4 import BeautifulSoup

def scrape_on_this_day_body(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        otd = soup.find(id='mp-otd')
        print(otd)
        events = otd.find_all('ul')[0]

        events2 = events.find_all('li')
        # for line in events2:
        #     print(line.text)
        #use events 2 to loop through 2 display on web
        return events2
    else:
        'Error with connection'


url = 'https://en.wikipedia.org/wiki/Main_Page'
# scrape_on_this_day_body(url)


def get_title(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find(id='mp-otd-h2')

            return title.text

    except Exception as e:
        print(f'Failed: {e}')

# print(get_title(url))

def get_paragraph(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            otd = soup.find(id='mp-otd')
            para = otd.find('p')
            return para.text

    except Exception as e:
        print(f'Failed: {e}')

get_paragraph(url)

import urllib
from urllib.parse import urljoin

def get_picture(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            image_div = soup.find(id='mp-otd-img')
            img_tag = image_div.find('img')
            src = img_tag.get('src')
            if src:
                src_url = urljoin(url, src)
                return src_url

    except Exception as e:
        print(f'Failed: {e}')


import urllib.request
#
# print(get_picture(url))
#
def download_image(url, save_as):
    image_url = get_picture(url)
    urllib.request.urlretrieve(image_url, save_as)

download_image(url, 'IMG_.png')




