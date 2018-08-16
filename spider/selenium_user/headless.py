from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('http://www.baidu.com')
print(driver.title)
#driver.save_screenshot('D:/baidu.png')
#输入长城
driver.find_element_by_id('kw').send_keys('萝莉')
#找到搜索按钮模拟点解
driver.find_element_by_id('su').click()
driver.save_screenshot('D:/萝莉.png')