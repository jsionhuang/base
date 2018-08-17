from bs4 import BeautifulSoup
soup = BeautifulSoup(open('./shein-www-2018-08-16_09.html',encoding='utf-8'),'html.parser')
#print(soup.select('div[class="init-j-top-banner"]'))#xpath选择器
#print(soup.title,soup.head,soup.a)#打印标签（tag），他有两个重要的属性 name  和 attrs
print(soup.head.name,soup.a.attr)#打印属性
#单独获得属性
#print(soup.script)
#print(soup.script['src'])
#对属性和内容进行修改
#soup.script['src'] = 'https://www.baidu.com'
#print(soup.script['src'])
#对属性进行删除
#del soup.script['async' ]
#遍历文档数
print(soup.select('div[class="init-j-top-banner"]')[0].contents[0])
topbannertag = soup.select('div[class="init-j-top-banner"]')[0]#往div要添加的字符串，生成方式
soup.select('div[class="init-j-top-banner"]')[0].append(topbannertag)#进行添加
print(soup.select('div[class="init-j-top-banner"]')[0].contents[0])
print(soup.prettify())
with open('test.html','a+',encoding='utf-8') as f:
    f.write(soup.prettify())
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
