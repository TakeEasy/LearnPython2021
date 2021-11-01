'''
作业：
1、文件内容如下,标题为:姓名,性别,年纪,薪资
    egon male 18 3000
    alex male 38 30000
    wupeiqi female 28 20000
    yuanhao female 28 10000

要求:
从文件中取出每一条记录放入列表中,
列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

2 根据1得到的列表,取出薪资最高的人的信息
3 根据1得到的列表,取出最年轻的人的信息
4、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写

5、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度

6、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）

7、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）

8、思考题

with open('a.txt') as f:
    g=(len(line) for line in f)
print(sum(g)) #为何报错？
9、文件shopping.txt内容如下

mac,20000,3
lenovo,3000,10
tesla,1000000,10
chicken,200,1
求总共花了多少钱？

打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]

求单价大于10000的商品信息,格式同上

10、思考：判断下述说法是否正确
    题目1：
    1、应该将程序所有功能都扔到一个模块中，然后通过导入模块的方式引用它们
    2、应该只将程序各部分组件共享的那一部分功能扔到一个模块中，然后通过导入模块的方式引用它们

    题目2：
    运行python文件与导入python文件的区别是什么？
    运行的python文件产生的名称空间何时回收，为什么？
    导入的python文件产生的名称空间何时回收，为什么？
'''

ALL_L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 123, 34567, 53456, 666666]


def binary_search(find_num, l):
    if len(l) == 1:
        print('找到了') if l[0] == find_num else print('没找到')
    else:
        mid_index = len(l) // 2
        if find_num > l[mid_index]:
            binary_search(find_num, l[mid_index + 1:])
        elif find_num < l[mid_index]:
            binary_search(find_num, l[:mid_index])
        else:
            print('找到了')


binary_search(4444, ALL_L)

new_l = (name + 1 for name in ALL_L)
print(type(new_l))
