# _*_ coding:utf‐8 _*
import hashlib
import random
import time
from selenium import webdriver
USER_AGENTS = [
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
my_app_key = "123"
app_secret = "123"
daili_url = 's5.proxy.mayidaili.com'
daili_port = '8123'
PROXY = "http://" + daili_url + ":" + daili_port

def proxy_info():  # 生成代理密鑰
    timesp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
    codes = app_secret + 'app_key' + my_app_key + 'timestamp' + timesp + app_secret
    sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()
    authHeader = 'MYH-AUTH-MD5 sign=' + sign + '&app_key=' + my_app_key + '×tamp=' + timesp
    return authHeader

if __name__ == '__main__':
    # 配置項目
    # Create a copy of desired capabilities object.
    # 在windows系統:chrome driver 默認使用的是IE代理設置。而例如Firefox可以自行配置proxy
    desired_capabilities = webdriver.DesiredCapabilities.SAFARI.copy()
    desired_capabilities['acceptSslCerts'] = True  # 忽略ssl 錯誤
    desired_capabilities['acceptInsecureCerts'] = True # 忽略ssl 錯誤
    # Change the proxy properties of that copy.
    desired_capabilities['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
    }
    # 創建的新實例驅動
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--proxy-bypass-list")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('user-agent=||{}||{}||'.format(random.choice(USER_AGENTS), proxy_info()))
    # options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=desired_capabilities)
    # 嘗試訪問登陸頁面
    for neti in range(0, 3):
        SUCCESS = True
        try:
            driver.get('https://www.baidu.com/')
            driver.implicitly_wait(10)  # wait seconds 等待頁面加載
        except Exception as e:
            SUCCESS = False
            print(e)
            continue
        if SUCCESS:
            break
    print(driver.page_source)
    print("--finish--")
    driver.quit()
    exit(0)