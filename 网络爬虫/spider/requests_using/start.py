import requests
from bs4 import BeautifulSoup
import random
res = requests.get('http://it.romwe.com')
soup = BeautifulSoup(res.text,'html.parser')
print(soup.prettify())
#with open('test.html','w',encoding='utf-8') as f:
    #f.write(soup.prettify())
for i in range(0,4):
    print(random.randint(0,4))
