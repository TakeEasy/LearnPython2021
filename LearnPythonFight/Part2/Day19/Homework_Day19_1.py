'''
1、文件内容如下,标题为:姓名,性别,年纪,薪资
egon male 18 3000
alex male 38 30000
wupeiqi female 28 20000
yuanhao female 28 10000

要求:
从文件中取出每一条记录放入列表中,
列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

2 根据1得到的列表,取出所有人的薪资之和
3 根据1得到的列表,取出所有的男人的名字
4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
5 根据1得到的列表,过滤掉名字以a开头的人的信息
6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值



# 选做作业：同昨天
'''


def range():
    x = 0
    while True:
        yield x
        x += 1


l = [1, 2, 3, 4, 5]
print(l.__iter__())


def dog(name):
    print('ahahahah %s' % name)
    while True:
        x = yield
        print('bbbbbbb %s' % x)


def print_list(li):
    for item in li:
        if type(item) is list:
            print_list(item)
        else:
            print(item)


def print_feibonaqi(x, y):
    print(x)
    print_feibonaqi(y, x + y)


print_feibonaqi(0, 1)
