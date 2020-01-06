import requests

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