from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin


def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

def task1(url):
    driver1 = driver()
    driver1.get(url)
    picture = driver1.find_element(By.XPATH, "//*[@id=\"mp-tfa-img\"]/div/span/a/img")
    picture = picture.get_attribute('src')
    print(picture)
    return picture


def download_image(url, file_name):
    d = task1(url)
    response = requests.get(d)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully: {file_name}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

url = 'https://en.wikipedia.org/wiki/Main_Page'
# download_image(url, 'pic.jpg')
# task1(url)
#***************************************************************************************************



# Not using Chrome Driver

from bs4 import BeautifulSoup

def get_src(url, target_src):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.findAll('img')
        for img in img_tags:
            src = img.get('src')

            if src and target_src in src:
                full_src = urljoin(url, src)
                return full_src

    except Exception as e:
        print(e)
        return False


def download_image_bs(url, target_src, file_name):
    src = get_src(url, target_src)

    image = requests.get(src)
    if image:
        try:
            with open(file_name, 'wb') as file:
                file.write(image.content)
                print('downloaded')

        except Exception as e:
            print('didnt download image')

    else:
        print('No link to download image')


# target_src = "//upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Fumio_Kishida_and_Hossein_Amir-Abdollahian_at_the_Kantei_2023_%281%29_%28cropped%29.jpg/120px-Fumio_Kishida_and_Hossein_Amir-Abdollahian_at_the_Kantei_2023_%281%29_%28cropped%29.jpg"
# download_image_bs(url, target_src, 'wiki3.jpg')


#**************************************************************************************************************


#Fastest way
#once you have the src and you add what is needed to make it a link that can be accessed through requests.
import urllib.request
scc = "//upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Fumio_Kishida_and_Hossein_Amir-Abdollahian_at_the_Kantei_2023_%281%29_%28cropped%29.jpg/120px-Fumio_Kishida_and_Hossein_Amir-Abdollahian_at_the_Kantei_2023_%281%29_%28cropped%29.jpg"


def download_image_urllib(url, scc, save_as):
    full_url = urljoin(url, scc)
    urllib.request.urlretrieve(full_url, save_as)

image_url = 'http://example.com/image.jpg'
save_as = 'image9.jpg'

download_image_urllib(image_url, scc, save_as)
















# task1('https://en.wikipedia.org/wiki/Main_Page')
# task1("https://www.geeksforgeeks.org/")



# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# time.sleep(3)

# try:
#     picture = WebDriverWait(driver1, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id=\"mp-tfa-img\"]/div/span/a/img"))
#     )
# except Exception as e:
#     print(e)