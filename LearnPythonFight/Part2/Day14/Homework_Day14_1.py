'''
1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表

# 选做作业：同昨天

'''


def howlong(something):
    return len(something) > 5


def cut_list(l):
    if len(l) > 2:
        return l[:2]
    else:
        return l


def odd_list(ll):
    new_l = []
    i = 0
    while i < len(ll):
        if i % 2 != 0:
            new_l.append(ll[i])
    return new_l


def cut_dict(dic):
    new_dict = {}
    for k, v in dic.items():
        if len(k) > 2:
            new_dict[k[0:2]] = v
        else:
            new_dict[k] = v
    return new_dict
