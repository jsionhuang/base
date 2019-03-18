import requests
import os
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options#使用heandless需要导入的内容
from bs4 import BeautifulSoup
import random
import pandas as pd
import time

from multiprocessing import Pool
STATIC_PATH = 'D:\\workfile\\topcms2\\app\static'#static目录
EXECEL_PATH = '{}/files/site_td.xlsx'.format(STATIC_PATH)#读取站点信息的excel表格地址
BASE_HTML_DIR = '{}/files/memo_htmls'.format(STATIC_PATH)#存放每个站点html文件和css，js的主目录
DRIVER_PATH = '{}/files/geckodriver.exe'.format(STATIC_PATH)

css = re.compile(r'href=\"(//.*?\/([0-9a-z\-_]*?\.css))')
png = re.compile(r'href=\"(//.*?\/([0-9a-z\-_]*?\.png))')
jss = re.compile(r'src=\"(//.*?\/([0-9a-z\-\._]*?\.js))')
png_src = re.compile(r'src=\"(//.*?\/([0-9a-z\-_]*?\.png))')
jpg_src = re.compile(r'src=\"(//[0-9a-z\-_\/\.]*?\/([0-9a-z\-_]*?\.jpg))')

#用于下载文件时候的保存
def save_files(url, html_path):
    file_name = '{}/{}'.format(html_path, url.split('/')[-1])
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers).content
    except Exception as inst:
        print(inst)
        resp = requests.get(url, headers=headers, verify=False).content
    with open(file_name, 'wb') as f:
        f.write(resp)

#保存文件，列如css和js文件
def download_files(content, html_path):
    for css_item in list(set([x[0] for x in css.findall(str(content))])):
        css_url = 'https:{}'.format(css_item)
        save_files(css_url, html_path)
    for jss_item in list(set([x[0] for x in jss.findall(str(content))])):
        jss_url = 'https:{}'.format(jss_item)
        save_files(jss_url, html_path)
    '''    
    for png_src_item in list(set([x[0] for x in png_src.findall(content)])):
        png_src_url = 'https:{}'.format(png_src_item)
        save_files(png_src_url, html_path)

    for jpg_src_item in list(set([x[0] for x in jpg_src.findall(content)])):
        jpg_src_url = 'https:{}'.format(jpg_src_item)
        save_files(jpg_src_url, html_path)
    '''

#下载html 文件，并且进行css和js文件的替换
def download_html(content, html_path, site_tp, site_id):
    memo_name = 'static/files/memo_htmls/{}/{}/{}'.format(site_tp, site_id, html_path.split('/')[-1])
    content = css.sub(r'href="/{}/\2'.format(memo_name), str(content))
    #content = png.sub(r'href="/{}/\2'.format(memo_name), content)
    content = jss.sub(r'src="/{}/\2'.format(memo_name), str(content))
    #content = png_src.sub(r'src="/{}/\2'.format(memo_name), content)
    #content = jpg_src.sub(r'src="/{}/\2'.format(memo_name), content)
    with open('{}.html'.format(html_path), 'w', encoding="utf-8") as f:
        f.write(content)

#将动态加载得到的top-banner 加载到由request得到 的shein的html界面
#有两个topnanner需要渲染
def update_shein_topbanner(site_url):
    dynamic_html_soup = get_dynamic_html(site_url)
    static_html_soup = get_static_html(site_url)
    top_banner_tag = dynamic_html_soup.select('div[class="init-j-top-banner"]')[0]
    tag = static_html_soup.select('div[class="init-j-top-banner"]')[0]
    tag.decompose()#删除节点
    staict_html_header = static_html_soup.select('header[class="c-header"]')[0]#获得tag所在位置
    staict_html_header.insert(0, top_banner_tag)#在指定位置插入节点
    #print(static_html_soup.prettify())
    return static_html_soup.prettify()

#将动态加载得到的top-banner 加载到由request得到 的romwe的html界面
#有一个topbanner需要渲染
def update_romwe_topbanner(site_url):
    static_soup = get_static_html(site_url)
    dynamic_soup = get_dynamic_html(site_url)
    #static_topbannners = static_soup1.select('div[viewed="true"]')
    dynamic_topbannner1 = dynamic_soup.select('div[viewed="true"]')[1]
    static_header = static_soup.select('header[class="c-header"]')[0]
    static_header.insert(1,dynamic_topbannner1)
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(static_soup.prettify())
    return static_soup.prettify()

#获得静态的界面
def get_static_html(site_url):
    headers_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    ]
    headers = {
        'user-agent': headers_list[random.randint(0,len(headers_list))-1],
        'Connection': 'keep - alive'
    }
    try:
        resp = requests.get(site_url, headers=headers)
    except Exception as inst:
        resp = requests.get(site_url, headers=headers, verify=False)
    soup = BeautifulSoup(resp.text, 'html.parser')
    time.sleep(3)
    return soup

#获得动态加载后的界面
def get_dynamic_html(site_url):
    executable_path = DRIVER_PATH
    firefox_options = Options()
    firefox_options.set_headless()
    driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=executable_path)
    print('selenium动态页面请求地址为', site_url)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    try:
        driver.get(site_url)
    except Exception as e:
        driver.execute_script('window.stop()')  # 超出时间则不加载
        print(e, '动态界面加载超出时间')
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    try:
        driver.quit()
    except:
        pass
    return soup

#进行备份
def backup_memo(bak_time, site_tp, site_id, site_url):
    print(site_tp,site_url)
    print(site_tp == 'shein',not(site_url.split('//')[1].startswith('m')))
    if (site_tp == 'shein') and not(site_url.split('//')[1].startswith('m')):
        print('开始备份shein动态界面，地址为',site_url)
        html_content = update_shein_topbanner(site_url)
    elif (site_tp == 'romwe') and not(site_url.split('//')[1].startswith('m')):
        print('开始备份romwe动态界面，地址为', site_url)
        html_content = update_romwe_topbanner(site_url)
    else:
        print('开始备份静态界面，地址为',site_url)
        html_content = get_static_html(site_url)
    #html文件存放的位置
    html_dir = BASE_HTML_DIR
    #html_dir = 'memo_htmls'
    html_path = '{}/{}/{}/{}-{}-{}'.format(html_dir, site_tp, site_id, site_tp, site_id, bak_time)
    if not os.path.exists(html_path):#文件夹不存在就创建按文件夹
        print('创建文件夹',html_path)
        os.makedirs(html_path)
        print('存放路径为：',html_path)
    download_files(html_content, html_path)
    download_html(html_content, html_path, site_tp, site_id)

def task():
    p = Pool(4)  # pool的默认大小是cpu的核数
    print('开始时间', datetime.now().strftime('%H:%M:%S'))
    bak_time = datetime.now().strftime('%Y-%m-%d_%H')
    file_path = EXECEL_PATH
    sites = pd.read_excel(file_path).values.tolist()
    for site in sites:
        site_tp = site[0].strip()
        site_id = site[1].strip()
        site_url = 'https://{}'.format(site[2].strip())
        try:
            print(site_url)
            p.apply_async(backup_memo, args=(bak_time, site_tp, site_id, site_url))
        except Exception as inst:
            print(inst)
    # backup_memo(bak_time, 'romwe', 'rwau', 'http://au.romwe.com')
    p.close()  # close之后就不能添加新的进程
    p.join()  # 会等待所有子程序执行完毕
    print('所有线程结束', '结束时间', time.strftime("%H:%M:%S"))

def time_task(h=0,m=0):
    while True:
        while True:
            now = datetime.now()
            if now.hour==h and now.minute==m:
                break
            time.sleep(20)#20秒检查一次
        task()
if __name__ == '__main__':
    time_task(11,32)
    time_task(17,00)





