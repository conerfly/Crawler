import requests
import os
path = "/Users/Johnny/Downloads/abc.jpg"
#url = "https://www.nationalgeographic.com/animals/2019/11/pharmaceuticals-pollution-dung-beetles-health/#/scarabs_07.jpg"
url = "http://img0.dili360.com/ga/M01/49/B7/wKgBzFqo7emAcq6PAATLZFhctQc857.tub.jpg@!rw17"
try:
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    # with open(path, 'wb') as f:
    #     f.write(r.content)
except:
    print("Get data error")