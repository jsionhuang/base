from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import requests
def headless(url):
    print('start:',time.strftime('%H:%M:%S'))
    try:
        fireFoxOption = Options()
        fireFoxOption.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOption,executable_path='./geckodriver.exe')
        driver.get(url)
        print(driver.title)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content,'html.parser')
        tags = soup.findChildren('header[class="c-header"]')
        print(tags)
        with open('broswer.html','w',encoding='utf-8') as f:
            f.write(soup.prettify())
    except Exception as e:
        print(e)
    finally:
        try:
            driver.close()
        except:
            pass
    print('end:', time.strftime('%H:%M:%S'))

def broswer():
    print('start:', time.strftime('%H:%M:%S'))
    driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    driver.get('https://www.shein.com')
    print(driver.title)
    print('end:', time.strftime('%H:%M:%S'))

def requests_using(url):
    print('start:', time.strftime('%H:%M:%S'))
    reps = requests.get(url)
    with open('test.html','w',encoding='utf-8') as f:
        f.write(reps.text)
    print('end:', time.strftime('%H:%M:%S'))


headless('https://us.romwe.com')
#broswer()
requests_using('https://us.romwe.com')