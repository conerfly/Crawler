import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text   #r.content是编码之前的返回值，r.text是编码之后返回的字符串
    except:
        print("获取html错误")
        return ""

def parsePag(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[i])  #eval函数的作用时去掉双引号
            title = eval(tlt[i].split(':')[i])
            ilt.append([price, title])
    except:
        print("解析错误")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  #定义表格头格式
    print(tplt.format("序号", "价格", "商品名"))
    count = 0
    for g in ilt:
        count = count +1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePag(infoList, html)
        except:
            print("main函数错误")
            continue
    printGoodsList(infoList)

main()