import requests

url = "https://www.baidu.com/s"
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
    print(len(r.text))
except:
    print("Get data error")