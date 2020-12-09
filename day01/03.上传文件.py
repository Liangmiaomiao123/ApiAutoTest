'''

'''

import requests

url="http://www.httpbin.org/post"
'''
#将本地的文件上传到服务器上

file="d:/text.txt"
file="d:\\text.txt"
file=r"d:\test.txt"

with open(file,encoding='utf-8',mode='r')as f:
    load={
        "file1":(file,f,"text/plain,f")#text/plain
    }

    r=requests.post(url,files=load)
    print(r.text）
          '''

#上传图片

file2="d:/test.jpg"

with open(file2,mode='rb') as f:
    load={
            #文件名:file-tuple
            #file-tuple可以是二元组、三元组、四元组

        "file2":(file2,f,"image/jpg")
        }
    r=requests.post(url,files=load)
    print(r.text)

#可以一次上传多个文件，文本和图片一起上传

# with open(file,mode='r',encoding='utf-8') as f2:
#     with open(file2,mode='rb')as f2:
#         load={
#             "file1":(file,f1),
#             "file2":(file2,f2,"image/jpn")
#         }
#         r=requests.post(url,file2=load)
#         print(r.text)