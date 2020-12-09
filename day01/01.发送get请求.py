'''
使用requests发送get请求
'''

import requests

#发送一个get请求，返回一个响应，将响应存到变量r中
r=requests.get("http://www.baidu.com")
#print(r.text)

#list获取用户列register http://192.168.150.54:8089/
url="http://192.168.150.54:8089//futureloan/mvc/api/member/list"
r=requests.get(url)#发送请求
#print(r.text)

#转换json格式

'''print(r.json())'''
r=r.json()

assert r['status']==1#对结果进行检查
assert r['code']=='10001'

#assert['msg']=='获取列表成功'


#get请求带参数，拼接到URL后面，?参数名1=参数值1&参数名2=参数值2
#注册额接口

#list获取用户列register http://192.168.150.54:8089/
url="http://192.168.150.54:8089//futureloan/mvc/api/member/register?mobilephone=15191855231&pwd=12345678"
r=requests.get(url)
r=r.json()
print(r)
assert r['status']==1
assert r['code']=='10001'
assert r['msg']=='注册成功'

url="http://192.168.150.54:8089//futureloan/mvc/api/member/register"
user={
    "mobilephone":"18989898989",
    "pwd":"123456",
    "regname":"hello"

}
r=requests.get(url,params=user)#发送请求
r=r.json()
print(r)

assert r['status']==0
assert r['code']=='20110'
assert r['msg']=='手机号码已被注册'
'''
url="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15129938653"
r=requests.get(url)
#不是json格式的不能调用
print(r.text)
'''
print(type(r))
print(r.status_code)#状态码
print(r.reason)#状态信息
print(r.cookies)
print(r.encoding)#编码方式
print(r.headers)#响应头
'''


#发送请求，带请求头
#有些网站，对自动化发出去的请求不处理,
#通过设置请求头，伪装浏览器发的请求。
#httpbin是一个测试网站，发送的请求，这个网站请求转成json格式的返回.

#header是请求头 使用requests发送的请求"User-Agent"为"python-requests/2.24.0",  user-Agent代表自动化发出的请求
url="http://www.httpbin.org/get?user=root&pwd=123123"
r=requests.get(url)
print(r.text)

head={
    "User-Agrnt":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"


}
r=requests.get(url,headers=head)
print(r.text)