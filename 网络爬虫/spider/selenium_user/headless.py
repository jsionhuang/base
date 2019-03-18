from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options = chrome_options)
driver.get('http://www.shein.com')
print(driver.title)
