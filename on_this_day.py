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
scrape_on_this_day_body(url)