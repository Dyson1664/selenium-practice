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


# url = 'https://en.wikipedia.org/wiki/Main_Page'
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

# get_paragraph(url)

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

def download_image(url, save_as):
    image_url = get_picture(url)
    urllib.request.urlretrieve(image_url, save_as)

import os
# os.makedirs(save_path, exist_ok=True)

def download_image_2_folder_flask(url):
    image_url = get_picture(url)
    save_path = r'C:\Users\PC\Desktop\practice\static\images'
    save_as = os.path.join(save_path, 'image.jpg')

    urllib.request.urlretrieve(image_url, save_as)


# download_image(url, 'IMG_.png')
# path = r"C:\Users\PC\Desktop\practice\IMG_.png"
def fetch_image(path):
    with open(path, 'rb') as file:
        content = file.read()
        return content


#now display it on a flask website

from flask import Flask, request, url_for, render_template

app = Flask('__name__')

app.secret_key = 'iewe678902345h#$@()*:><'



@app.route('/')
def wiki():
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    # path = r"C:\Users\PC\Desktop\practice\IMG_.png"

    wiki_title = get_title(url)
    paragraph = get_paragraph(url)
    bullets = scrape_on_this_day_body(url)

    download_image_2_folder_flask(url)
    print(wiki_title)

    return render_template('wiki.html', wiki_title=wiki_title, paragraph=paragraph, bullets=bullets)


def save_file(file_name ,info):
    with open(file_name, 'w') as file:
        file.write(info)

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return file.read()


import datetime

now = datetime.datetime.now()
print(now)
import time

url = 'https://en.wikipedia.org/wiki/Main_Page'
old = scrape_on_this_day_body(url)
save_file('html', old)

while True:
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    try:
        old = scrape_on_this_day_body(url)
        if old:

            time.sleep(3600)
            new = scrape_on_this_day_body(url)
            read = read_file('html')
        else:
            pass

    except Exception as e:
        print(f'Unable to scrape website and read file: {e}')

    try:
        if new and new != read:
            print('run function')
            url_for('wiki')
            delete_file(r"C:\Users\PC\Desktop\practice\html.txt")
            save_file('html', new)

        else:
            continue

    except Exception as e:
        print(e)




if __name__ == ('__main__'):
    app.run(debug=True)



#need to delete pic and loop for every day. Add some styling. Check if thats the best way to display a pic
#Bound to be a faster way of only scraping once