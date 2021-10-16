'''
1、有列表['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量

2、用列表的insert与pop方法模拟队列

3. 用列表的insert与pop方法模拟堆栈

4、简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数以三元组形式加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

5、有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中

即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

6、统计s='hello alex alex say hello sb sb'中每个单词的个数

'''

'''1、有列表['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量'''
li = ['alex', 49, [1900, 3, 18]]
name = li[0]
age = li[1]
born_year = li[2][0]
born_month = li[2][1]
born_day = li[2][2]

'''2、用列表的insert与pop方法模拟队列'''
li.insert(0, 11)
li.pop()

'''3. 用列表的insert与pop方法模拟堆栈'''
li.insert(len(li), 11)
li.pop()

'''4、简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数以三元组形式加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}'''
msg_dic = {
    'apple': 10,
    'tesla': 10000,
    'mac': 3000,
    'lenonvo': 30000,
    'chicken': 10
}
for item in msg_dic:
    print('{0}\t价钱:{1}'.format(item, msg_dic[item]))
shopping_car = []
while True:
    want_add = input('想买什么 Q/q退出:')
    if want_add.lower() in msg_dic:
        add_count = 0
        while True:
            str_add_count = input('购买数量')
            if str_add_count.isnumeric():
                add_count = int(str_add_count)
                break
            else:
                print('请输入数字')
        tuple_shopping_item = (want_add.lower(), msg_dic[want_add.lower()], add_count)
        shopping_car.append(tuple_shopping_item)

        print('添加成功')
        for l in shopping_car:
            print(l)
    elif want_add.lower() == 'q':
        print('购物结束')
        break
    else:
        print('没有这个商品')

'''5、有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中

即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}'''
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dict_num = {'k1': [], 'k2': []}
for i in li:
    if i > 66:
        dict_num['k1'].append(i)
    else:
        dict_num['k2'].append(i)
print(dict_num)

'''6、统计s='hello alex alex say hello sb sb'中每个单词的个数'''
s = 'hello alex alex say hello sb sb'
list_s = s.split(' ')
for i in list_s:
    print(len(i), end=' ')
