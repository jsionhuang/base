from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


#创建指定的浏览器对象
#driver = webdriver.PhantomJS()#如果没有在环境变量指定PhantomJS位置，就是将phantomjsdriver放入python的script文件中
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)#pip install selenium==2.48.0,3.0版本以上的selenium不支持
driver.set_window_size(1366,768)
#get,去请求对象url的界面,会等到页面加载结束，才会继续程序
driver.set_page_load_timeout(100)
driver.set_script_timeout(100)#这两
try:
    driver.get('https://www.shein.com/')
except:
    driver.execute_script('window.stop()')
    pass
#获得元素id为‘wraaper’的元素的文本
data = driver.page_source
#soup1 = BeautifulSoup(open('./broswer.html',encoding='utf-8'),'html.parser')
soup1 = BeautifulSoup(data,'html.parser')

topbannertags = soup1.select("div[class='init-j-top-banner']")[0]

soup2 = BeautifulSoup(open('./shein-www-2018-08-16_09.html',encoding='utf-8'),'html.parser')

tag = soup2.select('div[class="init-j-top-banner"]')[0]
print('删除节点')
tag.decompose()
print('在指定位置添加节点')
header = soup2.select('header[class="c-header"]')[0]
header.insert(0,topbannertags)
driver.quit()#直接退出

#print(soup2.prettify())
with open('test.html','a+',encoding='utf-8') as f:
    f.write(soup2.prettify())