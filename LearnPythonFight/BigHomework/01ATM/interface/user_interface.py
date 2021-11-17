'''
用户相关业务接口
'''
import json
import os
from config import settings
from db import db_handler
from lib import common

user_logger = common.get_logger('user')


def register_interface(username, password, balance=15000):
    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户名已存在'
    user_dic = {
        'username': username,
        'password': common.get_pwd_md5(password),
        'balance': balance,
        'flow': [],  # 用户流水
        'shop_car': {},  # 用户购物车
        'locked': False
    }
    db_handler.save(user_dic)
    return True, f'{username}注册成功'


def login_interface(username, password):
    user_dict = db_handler.select(username)

    if user_dict:
        if user_dict['locked']:
            return False, f'用户{username}已被锁定 无法登录'
        if common.get_pwd_md5(password) == user_dict.get('password'):
            return True, f'[{user_dict.get("username")}] 登录成功'
        else:
            return False, '密码错误'

    return False, '用户不存在'


def check_bal_interface(username):
    user_dict = db_handler.select(username)
    return user_dict.get('balance')
