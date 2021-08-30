import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('insert goods(name,price) '\
'values '\
"('Expensive box',200), "\
"('Affordable box',100), "\
"('Cheap box',50); "\
'insert orders(date) '\
'values '\
"('2021-07-25'), "\
"('2021-07-25'), "\
"('2021-08-26'), "\
"('2021-07-30'), "\
"('2021-08-01'); "\
'insert order_items(order_id,goods_id,quantity) '\
'values '\
'(1,1,2), '\
'(1,2,4), '\
'(2,3,200), '\
'(3,2,15), '\
'(3,2,20), '\
'(4,1,3)'), multi=True)
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
