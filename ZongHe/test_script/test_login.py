'''
登录接口测试脚本
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member,DbOp


@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_data(request):
    return request.param




@pytest.fixture(scope='module')
def register(setup_data,url,db,baserequests):
    print(f"测试数据:{setup_data}")
    # 获取手机号码
    mobile = setup_data['casedata']['mobilephone']
    Member.register(url, baserequests, setup_data['casedata'])
    #注册用户
    yield

    # 清理环境:删除注册用户

    DbOp.delete_user(db,mobile)
    #删除用户


def test_login(register,url,baserequests,db,login_data):
    # print(f"测试数据:{login_data}")
    # 下发登录的请求
    r=Member.login(url,baserequests,login_data['casedata'])



    #检查结果
    assert r.json()['msg']==login_data['expect']['msg']
    assert str(r.json()['code'])==str(login_data['expect']['code'])

