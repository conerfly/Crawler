import requests
from bs4 import BeautifulSoup

try:
    r = requests.get('https://www.baidu.com/index.php?tn=utf8kb_oem_dg')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
    # print(type(soup.head.attrs))   #查看soup标签的类型，beautifulsoup类一共有五种类型
except:
    print("error")
