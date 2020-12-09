'''
设置代理
1.如果想抓包分析自动化发出去的报文，可以通过设置代理抓包
2.用一台电脑频繁访问某个网站，被网站认为是攻击，将Ip地址禁用。设置代理，换一个Ip地址去访问。
'''
import requests
proxy={
    "http":"http://127.0.0.1:8888",#http协议，使用xxx代理
    "https":"https://127.0.0.1:8888"#https协议，使用xxx代理

 }
proxy={
    "http":None,
    "https":None
}

url="http://192.168.150.54:8089//futureloan/mvc/api/member/list"
r=requests.get(url,proxies=proxy)#给需要抓包的接口，设置代理
print(r.json())

url="http://192.168.150.54:8089//futureloan/mvc/api/member/register?mobilephone=15191855291&pwd=12345678"
r=requests.get(url,proxies=proxy)#给需要抓包的接口，设置代理
print(r.json())
