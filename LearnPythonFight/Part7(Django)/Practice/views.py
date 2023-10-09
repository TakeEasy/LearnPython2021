import datetime
from jinja2 import Template
import pymysql


def index(env):
    return 'Hellow login page'


def login(env):
    return 'Hellow index page'


def error(env):
    return 'Hellow error page'


def time(env):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %X')
    # 如何将后端的数据传给html的页面
    with open(r'templates/time.html', 'r', encoding='utf-8') as f:
        data = f.read()
    data = data.replace('@time', current_time)
    return data


def getDict(env):
    user_dict = {'username': 'Year', 'age': 18, 'hobby': 'read'}
    with open(r'templates/get_dict.html', 'r', encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user=user_dict)  # 给html页面传递了一个user值 页面上通过user能够拿到后端的user_dict
    return res


def getDB(env):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root123',
        db='learnpython2023',
        charset='utf8mb4',
        autocommit=True
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from userinfo'
    affect_rows = cursor.execute(sql)
    data_list = cursor.fetchall()
    print(data_list)
    with open(r'templates/get_db.html', 'r', encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user_list=data_list)
    return res


if __name__ == '__main__':
    getDB(111)
