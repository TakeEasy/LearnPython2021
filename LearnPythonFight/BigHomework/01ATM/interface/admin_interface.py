import json
import os
from config import settings
from db import db_handler
from lib import common

admin_logger = common.get_logger('admin')


def change_balance_interface(username, money):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '目标用户不存在'
    user_dic['balance'] = money
    return True, '修改成功'


def lock_user_interface(username):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '目标用户不存在'
    user_dic['locked'] = True
    return True, '冻结成功'
