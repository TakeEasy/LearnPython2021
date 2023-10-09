from wsgiref.simple_server import make_server
from urls import urls
from views import *

# def index(env):
#     return b'Hellow login page'
#
#
# def login(env):
#     return b'Hellow index page'
#
#
# def error(env):
#     return b'Hellow error page'
#
#
# urls = [
#     ('/index', index),
#     ('/login', login)
# ]


def run(env, response):
    """
    :param env:请求相关的所有数据
    :param response:相应相关的所有数据
    :return: 返回给浏览器的数据
    """
    print(env)  # 大字典,封装了所有的http相关格式数据 请求头和一些其他数据
    current_path = env.get('PATH_INFO')
    response('200 OK', [('XXX', 'OOO')])  # 响应首行 响应头
    # if current_path == '/index':
    #     return [b'Hellow index page']
    # elif current_path == '/login':
    #     return [b'Hellow login page']
    # else:
    #     return [b'Hellow wsgiref']
    func = None
    for url in urls:
        if current_path == url[0]:
            func = url[1]
            break
    if func:
        res = func(env)
    else:
        res = error(env)

    return [res.encode('utf-8')]
    # return [b'Hellow wsgiref']


if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, run)
    server.serve_forever()
    '''
    实时监听指定地址 只要有客户端连接请求进来
    交给run方法去处理
    
    falsk 启动源码
        make_server('127.0.0.1',8080,obj)
        __call__
    '''
