'''
银行相关接口
'''
import json
import os
from config import settings
from db import db_handler
from lib import common

bank_logger = common.get_logger('bank')


def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    balance = int(user_dic.get('balance'))
    money_need = int(money) * 1.05
    if 100 <= money <= balance:
        balance -= money_need
        user_dic['balance'] = balance
        flow = f'用户[{username}]提现{money}$成功,手续费:{money_need - float(money)}'
        user_dic[flow].append(flow)
        db_handler.save(user_dic)

        return True, flow

    return False, '提现失败'


def repay_interface(username, money):
    user_dic = db_handler.select(username)
    balance = user_dic.get('balance')
    balance += money
    user_dic['balance'] = balance
    flow = f'用户{username} 还款{money}成功'
    user_dic['flow'].append(flow)
    db_handler.save(user_dic)

    return True, flow


def transfer_interface(username, to_username, money):
    user_dic = db_handler.select(username)
    to_user_dic = db_handler.select(to_username)
    if not to_user_dic:
        return False, '目标用户不存在'
    if user_dic['balance'] >= money:
        user_dic['balance'] -= money
        to_user_dic['balance'] += money
        flow = f'用户{username}给用户{to_username}转账{money}'
        user_dic['flow'].append(flow)
        to_user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        db_handler.save(to_user_dic)
        return True, flow
    else:
        return False, '余额不够'


def check_flow(username):
    user_dic = db_handler.select(username)
    return user_dic['flow']


def pay_interface(username, cost):
    user_dic = db_handler.select(username)
    if user_dic.get('balance') >= cost:
        user_dic['balance'] -= cost
        flow = f'用户消费金额{cost}'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True
    return False
