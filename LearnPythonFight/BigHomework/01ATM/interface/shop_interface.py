'''
购物接口
'''
import json
import os
from config import settings
from db import db_handler
from lib import common
from interface import bank_interface


def shopping_interface(username, shoppingcar):
    cost = 0
    for price_number in shoppingcar.values():
        price, number = price_number
        cost += (price * number)

    flag = bank_interface.pay_interface(username, cost)
    if flag:
        return True, '支付成功'
    return False, '余额不足'


def add_shopcar_interface(username, shoppingcar):
    user_dic = db_handler.select(username)
    for shop_name, price_number in shoppingcar.items():
        if shop_name in user_dic.get('shop_car'):
            user_dic['shop_car'][shop_name] += price_number[1]
        else:
            user_dic['shop_car'].update({shop_name: price_number})
    return True, '添加购物车成功'
