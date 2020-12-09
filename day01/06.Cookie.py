'''
登录以后的接口
Cookie:
http协议：无状态、无连接、媒体独立
每个请求都是独立的。有一些接口登录后才能访问，需要使用Cookie验证用户是否登录。
account/dashboard如果没有登录了，返回登录的页面。
account/dashboard如果登录了，返回用户详细信息。浏览器登录后，获取到的cookie直接放到自动化来用。
如果cookie失效或者换其他用户登录，就不能继续访问。

'''

import requests
#百格网站，有一些接口登录之后才能访问。

url="https://www.bagevent.com/account/dashboard"
r=requests.get(url)
print(r.text)

#用fiddler抓到的包，将里边的头设置到这里

head={
    "Cookie":'MEIQIA_TRACK_ID=1l8RRSG0WhaGluOUwPptzq2x3zf; __auc=fefd464e1762746d844af04542f; _ga=GA1.2.1026400383.1606976741; __asc=65b6de771762cc19cf729297f96; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976720,1607068655; MEIQIA_VISIT_ID=1lBRmgA0q4GzygHfVamcEv31Re2; _gid=GA1.2.827940995.1607068666; BAGSESSIONID=a2397f6b-aa4f-4699-95f0-1b7477f51c49; JSESSIONID=2DDE08A5F763671880FECB4804AE82BA; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607070328; _gat=1; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'

   # "Cookie": 'MEIQIA_TRACK_ID=1l8RRSG0WhaGluOUwPptzq2x3zf; __auc=fefd464e1762746d844af04542f; _ga=GA1.2.1026400383.1606976741; __asc=65b6de771762cc19cf729297f96; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976720,1607068655; MEIQIA_VISIT_ID=1lBRmgA0q4GzygHfVamcEv31Re2; BAGSESSIONID=b3553085-92be-4878-9836-af7b84d7c036; JSESSIONID=9774859408C23E5932D8D98796A202DE; _gid=GA1.2.827940995.1607068666; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068666; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'
}

print("登录后，返回的结果为:")

r=requests.get(url,headers=head)

print(r.text)