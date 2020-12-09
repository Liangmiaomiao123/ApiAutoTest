
#
import requests
import random

'''注册'''

#20103：参数错误：参数不能为空
# #1.验证手机号为空，密码注册名正常填写，注册失败
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=&pwd=123456&regname=1"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20103'
# assert r['msg']=='手机号不能为空'
#
# #2.验证手机号，注册名正确填写，密码不输入，注册失败
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15126654325&pwd=&regname=1"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20103'
# assert r['msg']=='密码不能为空'

# #3手机号注册名密码填写，密码，注册名不输入，注册成功
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15126654329&pwd=123456&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='注册成功'
#
# #4.20109：手机号码格式不正确
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=99126654329&pwd=123456&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20109'
# assert r['msg']=='手机号码格式不正确'

#20110：手机号码已被注册
# #1.验证已存在手机号，正确密码长度，不输入注册名
#
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=25129938764&pwd=123456&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20110'
# assert r['msg']=='手机号码已被注册'

# #2.验证已存在手机号，正确密码长度，输入注册名
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15129938764&pwd=123456&regname=er"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20110'
# assert r['msg']=='手机号码已被注册'

#20108：密码长度必须为6~18
# #1.验证新手机号，密码输入5位，输入注册名
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15629938764&pwd=12345&regname="ht"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20108'
# assert r['msg']=='密码长度必须为6~18'
# #2.验证新手机号，密码输入6位，输入注册名
#
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15639938764&pwd=123457&regname=12"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='注册成功'

#3.验证新手机号，密码输入18位，输入注册名
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15679938764&pwd=123456789123456787&regname=12"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='注册成功'

# #4.验证新手机号，密码输入19位，输入注册名
#
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15679638764&pwd=1234567891234567878&regname=12"
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20108'
# assert r['msg']=='密码长度必须为6~18'

# #5.验证新手机号，密码输入5位，不输入注册名
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15629938764&pwd=12345&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20108'
# assert r['msg']=='密码长度必须为6~18'

# #2.验证新手机号，密码输入6位，不输入注册名
#
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15639938764&pwd=123457&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='注册成功'

#3.验证新手机号，密码输入18位，不输入注册名
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15679938764&pwd=123456789123456787&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='注册成功'

# #4.验证新手机号，密码输入19位，不输入注册名
#
# url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=15679638764&pwd=1234567891234567878&regname="
# r=requests.get(url)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20108'
# assert r['msg']=='密码长度必须为6~18'

'''登录'''

#20103：参数错误：参数不能为空

# #1.手机号不输入，密码输入（正确格式、不正确格式）进行登录，登录失败
#
# url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
# user={
#     "mobilephone":"",
#     "pwd":"12345"
# }
# r=requests.post(url,data=user)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20103'
# assert r['msg']=='手机号不能为空'

# #2.输入已注册手机号，密码不输入，登录失败
# url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
# user={
#     "mobilephone":"15129938653",
#     "pwd":""
# }
# r=requests.post(url,data=user)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20103'
# assert r['msg']=='密码不能为空'

# #3.输入未注册手机号（或错误手机号），密码不输入，登录失败
# url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
# user={
#     "mobilephone":"@73897652",
#     "pwd":""
# }
# r=requests.post(url,data=user)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20103'
# assert r['msg']=='密码不能为空'
#
# #20111：用户名或者密码错误
# headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
#                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
#                "186", "187", "188", "189"]
# phone=(random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
# #1.输入未注册手机号（或错误手机号），密码输入(长度正确，长度不正确)，登录失败
#
# url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
# user={
#     "mobilephone":"12345",
#     "pwd":"12345"
# }
# r=requests.post(url,data=user)
# r=r.json()
# print(r)
# assert r['status']==0
# assert r['code']=='20111'
# assert r['msg']=='用户名或密码错误'
#
# #2.输入已注册手机号，不正确密码，登录失败
#
# url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
# user={
#     "mobilephone":"15126654329",
#     "pwd":"123456"
# }
# r=requests.post(url,data=user)
# r=r.json()
# print(r)
# assert r['status']==1
# assert r['code']=='10001'
# assert r['msg']=='登录成功'

'''投资记录'''
#30203：参数错误：参数不能为空
#1.验证id为空时，查看投资记录失败
url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id="
r=requests.get(url)
r=r.json()
assert r['status']==0
assert r['code']=='30203'
assert r['msg']=='参数错误：参数不能为空'

#2.验证输入字母的id进行查看投资记录，查询失败

url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id=adcgfb"
r=requests.get(url)
r=r.json()
assert r['status']==0
assert r['code']=='30104'
assert r['msg']=='参数错误，参数必须是数字'

#3.验证输入字母加数字组合，查看投资记录失败
url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id=adc123"
r=requests.get(url)
r=r.json()
assert r['status']==0
assert r['code']=='30104'
assert r['msg']=='参数错误，参数必须是数字'
#4.验证特殊字符id，查看投资记录失败
url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id=#$%23"
r=requests.get(url)
r=r.json()
assert r['status']==0
assert r['code']=='30104'
assert r['msg']=='参数错误，参数必须是数字'
#5.验证纯数字的id但是系统不存在的id，查看投资记录失败
url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id=43546587987"
r=requests.get(url)
r=r.json()
assert r['status']==0
assert r['code']=='30104'
assert r['msg']==''
#6验证纯数字的id系统存在，查询成功
url="http://192.168.150.54:8090/futureloan/mvc/invest/getInvestsByLoanId?id=6587987"
r=requests.get(url)
r=r.json()
assert r['status']==1
assert r['code']=='10001'
assert r['msg']=='成功'

