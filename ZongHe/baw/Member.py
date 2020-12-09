'''
Member模块的接口

'''

def register(url,basequests,data):

    '''
    注册接口
    :param url: 环境信息，比如http://jy001:8081/
    :param basequests: Basequests的实例
    :param data: 注册的测试数据
    :return: 响应信息
    '''
    url=url+"futureloan/mvc/api/member/register"
    r=basequests.post(url,data=data)
    return r

def user_list(url,basequests):
    url1=url+"futureloan/mvc/api/member/list"
    r1=basequests.post(url1)
    return r1


def login(url,basequests,data):
    url2=url+"/futureloan/mvc/api/member/login"
    r2=basequests.post(url2)
    return r2

if __name__ == '__main__':

    from ZongHe.caw.BaseRequest import BaseRequests

    b=BaseRequests()
    canshu={'mobilephone':"15123487654","pwd":"123456"}
    r=register("http://jy001:8081/",b,canshu)
    print(r)