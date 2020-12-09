'''
发动post请求
'''
import requests

#登录的接口:
url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
user={
    "mobilephone":"15129938653",
    "pwd":"123456"
}


#用data传表单参数，content-type: "application/x-www-form-urlencoded",表单格式
r=requests.post(url,data=user)
print(r.text)

#
url="http://www.httpbin.org/post"
user={
    "mobilephone":"15656778",
    "pwd":"123456"
}

r=requests.post(url,data=user)
print(r.text)

print("******")


#用json传参数，  "Content-Type": "application/json",

r=requests.post(url,json=user)#是data还是json传参，要看接口实现的是哪个
#如果返回的是json格式的要转成json
print(r.text)
'''
assert r.json()['status']==1
assert r.json()['data']['regname']=='15029938654'
print(r.json()['data']['leaveamount'])
'''

print("******")
'''
#练习：充值接口，给注册的用户充值
#充值的接口地址
url="http://192.168.150.54:8089//futureloan/mvc/api/member/recharge"
user={
    "mobilephone":"15129938653",
    "amount":"500001"
}
r=requests.post(url,data=user)
print(r.text)
'''
#验证手机号、密码、注册名不输入，注册失败
