'''
注册的脚本
'''
#测试数据
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member
from ZongHe.baw import DbOp

#测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case/register_success.yaml"))
def success_data(request):
    return request.param

#测试逻辑
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据:{fail_data}")

    #下发注册的请求
    r=Member.register(url,baserequests,fail_data['data'])
    print(r.text)
    #校验结果

    assert r.json()['msg']==fail_data['expect']['msg']

    assert r.json()['code']== fail_data['expect']['code']

def test_register_success(success_data,url,db,baserequests):
    #下发注册的请求
    #检查结果，1:检查响应与预期结果一致
    #检查结果:2:检查系统中用户注册成功
    #清理环境：删除注册用户
    print(f"测试数据:{success_data}")
    #获取手机号码
    mobile=success_data['data']['mobilephone']
    print(mobile)

    # DbOp.delete_user(db, mobile)

    r=Member.register(url,baserequests,success_data['data'])
    print(r.text)

    #检查结果15375632187
    assert r.json()['msg']==success_data['expect']['msg']
    assert str(r.json()['code'])==str(success_data['expect']['code'])
    assert r.json()['status']==success_data['expect']['status']


    #检查结果，2检查系统中用户注册成功
    #查询用户，检查手机号在返回的结果中

    r=Member.user_list(url,baserequests)
    assert mobile in r.text



    # mobiles=DbOp.select_user(db,mobile)
    # assert len(mobiles)==1

    #清理环境:删除注册用户

    DbOp.delete_user(db,mobile)

