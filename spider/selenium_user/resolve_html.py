from bs4 import BeautifulSoup
import bs4
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
#print(soup.select('div[class="init-j-top-banner"]'))#xpath选择器
#print(soup.title,soup.head,soup.a)#打印标签（tag），他有两个重要的属性 name  和 attrs
#print(soup.head.name,soup.a.attr)#打印属性
#单独获得属性
#print(soup.script)
#print(soup.script['src'])
#对属性和内容进行修改
#soup.script['src'] = 'https://www.baidu.com'
#print(soup.script['src'])
#对属性进行删除
#del soup.script['async' ]
#遍历文档数
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


    except Exception as e:
        print(e)
    finally:
        try:
            driver.close()
        except:
            pass
    print('end:', time.strftime('%H:%M:%S'))
    return soup

def broswer(url):
    print('start:', time.strftime('%H:%M:%S'))
    driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    driver.get(url)

    print('end:', time.strftime('%H:%M:%S'))

def requests_using(url):
    print('start:', time.strftime('%H:%M:%S'))
    reps = requests.get(url)
    soup = BeautifulSoup(reps.text,'html.parser')
    print('end:', time.strftime('%H:%M:%S'))
    return soup
soup1 = requests_using('http://au.romwe.com')
soup2 = headless('http://au.romwe.com')
s1 = soup1.select('header[class="c-header"]')[0]
s2 = soup2.select('header[class="c-header"]')[0]

#print(soup.select('header[class="c-header"]')[0].children)


#print(s.contents)
pare = soup1.select('header[class="c-header"]')[0]
s2_tage1 = soup2.select('div[viewed="true"]')[0]
s2_tage2 = soup2.select('div[viewed="true"]')[1]
print('动态加载内容1',s2_tage1)
print('动态加载内容2',type(s2_tage2),s2_tage2)
pare.insert(1,s2_tage2)
#print(s.contents)
with open('test.html','w',encoding='utf-8') as f:
    f.write(soup1.prettify())
#topbannertag = soup.select('div[class="init-j-top-banner"]')[0]#往div要添加的字符串，生成方式
#oup.select('div[class="init-j-top-banner"]')[0].append(topbannertag)#进行添加
#print(soup.select('div[class="init-j-top-banner"]')[0].contents[0])
#print(soup.prettify())
#with open('test.html','a+',encoding='utf-8') as f:
#    f.write(soup.prettify())
''' 
    前八种是单一元素的定位选取
    1.id定位：find_element_by_id(self, id_)
    2.name定位：find_element_by_name(self, name)
    3.class定位：find_element_by_class_name(self, name)
    4.tag定位：find_element_by_tag_name(self, name)
    5.link定位：find_element_by_link_text(self, link_text)
    6.partial_link定位find_element_by_partial_link_text(self,link_text)
    7.xpath定位：find_element_by_xpath(self, xpath)
    8.css定位：find_element_by_css_selector(self,css_selector）
    这八种是以上的复数形式，结果返回为list形式，因为之前的BeatifulSoup.select()同样返回list，故这几种可能用起来更方便
    9.id复数定位find_elements_by_id(self, id_)
    10.name复数定位find_elements_by_name(self, name)
    11.class复数定位find_elements_by_class_name(self, name)
    12.tag复数定位find_elements_by_tag_name(self, name)
    13.link复数定位find_elements_by_link_text(self, text)
    14.partial_link复数定位find_elements_by_partial_link_text(self,link_text)
    15.xpath复数定位find_elements_by_xpath(self, xpath)
    16.css复数定位find_elements_by_css_selector(self,css_selector
    还有两种不怎样用的
    find_element(self, by='id', value=None)find_elements(self, by='id', value=None)'''
