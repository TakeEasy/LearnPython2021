'''
用户输入姓名、年龄、工作、爱好 ，然后打印成以下格式
------------ info of Egon -----------
Name  : Egon
Age   : 22
Sex   : male
Job   : Teacher
------------- end -----------------
'''
NAME = 'YEAR'
AGE = 28
SEX = 'male'
JOB = 'PA'
print('{0:*^20}'.format('Info of {0}').format(NAME))
print('Name:{0}'.format(NAME))
print('Age:{0}'.format(AGE))
print('Sex:{0}'.format(SEX))
print('Job:{0}'.format(JOB))
print('{0:*^20}'.format('End'))

'''用户输入账号密码，程序分别单独判断账号与密码是否正确，正确输出True，错误输出False即可'''
ACCOUNT_DICT = {'username': 'year', 'password': 'year93926'}
username_input = input('Pls input your username:')
print(username_input == ACCOUNT_DICT['username'])
pwd_input = input('Pls input your password:')
print(pwd_input == ACCOUNT_DICT['password'])

'''让计算机提前记下egon的年龄为18岁，写一个才年龄的程序，要求用户输入所猜的年龄
，然后程序拿到用户输入的年龄与egon的年龄比较，输出比较结果即可'''
age_input = input('Pls input your age:')
print(int(age_input) == AGE)

'''程序从数据库中取出来10000条数据，打算显示到页面中，
但一个页面最多显示30条数据,请选取合适的算数运算符，计算
   显示满30条数据的页面总共有多少个？
   最后一页显示几条数据？'''

print('pagecounts:{0}  lastpagerows:{1}'.format(10000 // 30, 10000 % 30))

'''egon今年为18岁，请用增量赋值计算3年后egon老师的年龄'''
AGE = 18
AGE += 3
print('{0}'.format(AGE))

'''将值10一次性赋值给变量名x、y、z'''
x = y = z = 10

'''请将下面的值关联到它应该对应的变量名上，你懂的
dsb = "egon"
superman = "alex"'''
dsb = 'egon'
superman = 'alex'
print('{0},{1}'.format(dsb, superman))
dsb, superman = superman, dsb
print('{0},{1}'.format(dsb, superman))

'''我们只需要将列表中的傻逼解压出来，一次性赋值给对应的变量名即可
names=['alex_sb','wusir_sb','oldboy_sb','egon_nb','lxx_nb','tank_nb']'''
names = ['alex_sb', 'wusir_sb', 'oldboy_sb', 'egon_nb', 'lxx_nb', 'tank_nb']
sb1, sb2, sb3, sb4, sb5, sb6 = names
print(sb1, sb2, sb3, sb4, sb5, sb6)
