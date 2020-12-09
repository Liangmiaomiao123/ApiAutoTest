'''

脚本层的公共方法
'''
import os
import sys


def get_project_path():
    '''
    获取工程路径
    :return: 当前工程路径，比如E:\ApiAutoTest\ZongHe\
    '''
    # __file__ 存储着当前文件的路径
    path = os.path.realpath(__file__)
    # 上一级目录
    path = os.path.dirname(path)
    # 再上一级目录
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    return path + "\\"

print(get_project_path())
sys.path.append(get_project_path())

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


