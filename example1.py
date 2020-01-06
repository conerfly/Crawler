import requests
url = "https://item.jd.com/100003150683.html"
try:
    r = requests.get(url)
    r.raise_for_status()     #网站返回的代码如果是200的情况下不返回异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("Get Data fail")


#访问亚马逊
am_url = "https://www.amazon.cn/dp/B06XYJQSGX?ref_=Oct_DLandingS_D_9e701ac6_60&smid=A26HDXW89ZT98L"
kv = {'user-agent':'Mozilla/5.0'}
try:
    re = requests.get(am_url, headers = kv)
    re.raise_for_status()
    print(re.text)
    re.encoding = re.apparent_encoding
    print(re.text[:1000])
except:
    print("Get Data fail")