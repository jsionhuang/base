from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
def headless():
    print('start:',time.strftime('%H:%M:%S'))
    try:
        fireFoxOption = Options()
        fireFoxOption.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOption,executable_path='./geckodriver.exe')
        driver.get('https://shein.com')
        print(driver.title)
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
    driver.get('https://shein.com')
    print(driver.title)
    print('end:', time.strftime('%H:%M:%S'))

headless()
broswer()