'''

'''

import requests
from unittest import mock
#取现接口未实现，写一个取现成功的用例。

class Pay:
    def zhifu2(self,data):
        r=requests.post("http://www.member.withdraw.com/",data=data)
        return r.json()

def tixian():
    pay = Pay()
    pay.tixian = mock.Mock(return_value={"code": 200, "msg": "提现成功"})
    canshu = {"订单号": "12345", "提款金额": 20.56, "支付方式": "银行卡"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "提现成功"


