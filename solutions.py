# 1 10 3 9 10 1


# def foo(m):
#     s = 0
#     for i in range(len(m)):  # 0 1 2
#         b = 0
#         for j in range(len(m)):  # 2
#             if m[i] == m[j]:
#                 b += 1
#         if b == 1:
#             s = s + m[i]
#     return s


# print(foo([10, 4, 4]))

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
# http://www.mysqltutorial.org/python-mysql/
# https://speakerdeck.com/dshafik/introduction-to-databases?slide=35

import mysql.connector

cnx = mysql.connector.connect(
    user='root', password='1', host='127.0.0.1', database='bootcamp')

cursor = cnx.cursor()

query = ("select * from products")

cursor.execute(query)

for data in cursor:
    print(data)

cnx.cursor()
cnx.close()
