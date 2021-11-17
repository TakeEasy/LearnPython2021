'''用户视图层'''
import sys
import os
from interface import user_interface, bank_interface, admin_interface, shop_interface
from lib import common

login_user = None


# 注册功能
def register():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        input_re_password = input('请确认密码:').strip()

        if input_password == input_re_password:
            flag, msg = user_interface.register_interface(input_username, input_password, 15000)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 登录功能
def login():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        flag, msg = user_interface.login_interface(input_username, input_password)
        if flag:
            global login_user
            print(msg)
            login_user = input_username
            break
        else:
            print(msg)


# 查看余额
@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(login_user)
    print(f'用户{login_user} 账户余额:{balance}')


# 提现功能
@common.login_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额:').strip()
        if not input_money.isdigit():
            print('请输入数字')
            continue
        input_money = int(input_money)
        flag, msg = bank_interface.withdraw_interface(login_user, input_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

    # 还款功能


@common.login_auth
def repay():
    while True:
        input_money = input('请输入还款金额:').strip()
        if not input_money.isdigit():
            print('请输入数字')
            continue
        input_money = int(input_money)
        if input_money > 0:
            flag, msg = bank_interface.repay_interface(login_user, input_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 转账功能
@common.login_auth
def transfer():
    while True:
        input_money = input('请输入转账金额:').strip()
        input_to_user = input('请转入用户:').strip()
        if not input_money.isdigit():
            print('请输入数字')
            continue
        input_money = int(input_money)
        if input_money > 0:
            flag, msg = bank_interface.transfer_interface(login_user, input_to_user, input_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 查看流水
@common.login_auth
def check_flow():
    flow_list = bank_interface.check_flow(login_user)
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('暂时没有流水')


# 购物功能
@common.login_auth
def shopping():
    # shop_list = {
    #    '0': {'name': 'haha', 'price': 30},
    # }
    shopping_car = {}
    shop_list = [
        ['hahah', 30],
        ['hehe', 100],
        ['iphone', 200],
        ['oneplus', 1000],
        ['xiaomi', 500],
        ['huawei', 800],
        ['sanxing', 999],
    ]
    while True:
        for index, shop in enumerate(shop_list):
            shop_name, shop_price = shop
            print(f'{index}:{shop_name} 价格:{shop_price}')
        choice = input('请输入购买商品编号 (y结算,n添加购物车):').strip()

        if choice == 'y':
            if not shopping_car:
                print('购物车是空的')
                continue
            flag, msg = shop_interface.shopping_interface()
            if flag:
                print(msg)
                break
            else:
                print(msg)
        elif choice == 'n':
            flag, msg = shop_interface.add_shopcar_interface(login_user,shopping_car)

            if flag:
                print(msg)
                break

        if not choice.isdigit():
            continue
        choice = int(choice)
        if choice not in range(len(shop_list)):
            print('商品不存在')
            continue
        shop_name, shop_price = shop_list[choice]

        if shop_name in shopping_car:
            shopping_car[shop_name][1] += 1
        else:
            shopping_car[shop_name] = [shop_price, 1]


# 查看购物车
@common.login_auth
def check_shop_car():
    pass


# 管理员功能
def add_user():
    register()


def change_balance():
    while True:
        change_user = input('请输入需要修改额度的用户:').strip()
        money = input('请输入修改的额度:').strip()
        if not money.isdigit():
            continue
        money = int(money)
        flag, msg = admin_interface.change_balance_interface(change_user, money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def lock_user():
    while True:
        lcok_user = input('请输入需要锁定的用户:').strip()
        flag, msg = admin_interface.lock_user_interface(lcok_user)
        if flag:
            print(msg)
            break
        else:
            print(msg)


admin_func = {
    '1': add_user,
    '2': change_balance,
    '3': lock_user,
}


@common.login_auth
def admin():
    while True:
        print('''
        1.添加账户
        2.修改额度
        3.冻结账户
        ''')
        choice = input('请输入管理员功能编号:').strip()
        if choice not in admin_func:
            print('请输入正确的功能编号!')
            continue

        admin_func.get(choice)()
        break


# func dict
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin
}


def run():
    while True:
        print('''
        -----ATM+购物车-----
            1、注册功能
            2、登录功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        --------end--------
        ''')

        choice = input('请输入功能编号:').strip()
        if choice not in func_dic:
            print('请输入正确的功能编号!')
            continue

        func_dic.get(choice)()
