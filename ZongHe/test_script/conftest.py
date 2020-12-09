'''

脚本层的公共方法
'''

import pytest
from ZongHe.caw import DataRead

from ZongHe.caw.BaseRequest import BaseRequests

@pytest.fixture(scope='session')

def url():
    return DataRead.read_ini('data_env/env.ini',"url")

#创建一个BaseRequests的实例，整个执行过程使用这个实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()

#从环境文件中读db信息，整个过程一次读
@pytest.fixture(scope='session')
def db():
    info=DataRead.read_ini('data_env/env.ini',"db")

    print(type(info))
    print(type(eval(info)))

    return eval(info) #将字符串解析成字典


