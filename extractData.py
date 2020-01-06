from bs4 import BeautifulSoup
import requests
import re

r = requests.get('https://cn.bing.com/academic/?FORM=Z9LH2')
soup = BeautifulSoup(r.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

# 利用find_all提取html信息, 查找属性id为link的节点
soup.find_all(id='link')
#查找名称为p的含有course属性值的标签
soup.find_all('p', 'course')
#利用正则表达式找到所有包含link的属性
soup.find_all(id=re.compile('link'))