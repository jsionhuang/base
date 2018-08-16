from selenium import webdriver
#创建指定的浏览器对象
#driver = webdriver.PhantomJS()#如果没有在环境变量指定PhantomJS位置，就是将phantomjsdriver放入python的script文件中
driver = webdriver.PhantomJS(executable_path = "./phantomjs")
driver.set_window_size(1366,768)
#get,去请求对象url的界面,会等到页面加载结束，才会继续程序
driver.get('http://baidu.com')
#获得元素id为‘wraaper’的元素的文本
data = driver.find_element_by_id('wrapper').text
print(data)