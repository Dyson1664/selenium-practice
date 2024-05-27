from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests


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
download_image(url, 'pic.jpg')

#***************************************************************************************************

# Not using Chrome Driver


# def download_via_requets(url):



















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