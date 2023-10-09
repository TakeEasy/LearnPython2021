import pymysql

# from pymysql import cursors
# import datetime
# cursors.DictCursor

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root123',
    database='learnpython2023',
    charset='utf8mb4'
)

# cursor = conn.cursor()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from test_book where title=%s and price=%d;'
res = cursor.execute(sql, ('book1', 100))

print(cursor.fetchone())
print(cursor.fetchall())
cursor.scroll(1, 'relative')
