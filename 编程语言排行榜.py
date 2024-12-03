import requests
import re

f = open("编程语言排行榜.csv", mode="w", encoding='utf-8')

url = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(url)
resp.encoding = "utf-8"
pageSource = resp.text

obj = re.compile(r'<td>(?P<num1>\d+)</td><td>(?P<num2>\d+)</td><t'
                 r'd>.*?</td>.*?<td>(?P<name>.*?)</td><td>(?P<bai>\d+\.?\d*%)</t'
                 r'd><td>(?P<creat>.*?)</td>', re.S)
result = obj.finditer(pageSource)
for item in result:
    num1 = item.group("num1")
    num2 = item.group("num2")
    name = item.group("name")
    bai = item.group("bai")
    creat = item.group("creat")
    f.write(f"{num1},{num2},{name},{bai},{creat}\n")

f.close()
resp.close()
print("编程语言排行榜提取完毕")