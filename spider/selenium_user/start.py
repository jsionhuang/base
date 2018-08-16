##驱动下载地址 http://chromedriver.storage.googleapis.com/index.html
#chromedriver v2.29 对应 chromed68版本
from  selenium import webdriver

#browser_chromed = webdriver.Chrome()#谷歌浏览器，驱动直接放到python的目录上面
browser_phantom = webdriver.PhantomJS()#将phantomJS的exe直接放到python的Script的目录下面
browser_phantom.get('http://www.baidu.com/')
#browser_chromed.get('http://www.baidu.com/')
print(browser_phantom.title)
print(browser_phantom.page_source)