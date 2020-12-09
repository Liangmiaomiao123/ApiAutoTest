'''
#练习：注册接口的测试代码，用这种方式来实现

'''

import pytest
import requests

@pytest.fixture(params=[
    {"data":{"mobilephone":"15634275438","pwd":"","regname":"we"},"expect":{"msg":"密码不能为空","code":"20103"}},
    {"data":{"mobilephone":"15124456792","pwd":"12345678","regname":"we"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
    {"data":{"mobilephone":"15124456781","pwd":"1234","regname":"we"},"expect":{"msg":"密码长度必须为6~18","code":"20108"}}
])
def zhuce_data(request):#参数request是固定的，不能写成其他
    return request.param


def test_zhuce(zhuce_data):
    url="http://192.168.150.54:8089//futureloan/mvc/api/member/register"

    print("测试数据",zhuce_data['data'])
    print("预期结果",zhuce_data['expect'])
    r = requests.post(url,data=zhuce_data['data'])
    print(r.text)
    assert r.json()['msg']==zhuce_data['expect']['msg']
    assert r.json()['code']==zhuce_data['expect']['code']


# def test_zhuce(zhuce_data):
#     url="http://192.168.150.54:8089//futureloan/mvc/api/member/register"
#     r = requests.get(url, params=zhuce_data['data'])  # 发送请求
#     r = r.json()
#     print(r)




