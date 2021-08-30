import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute((
'(id int primary key auto_increment, '\
  'goods_id int, '\
  'foreign key(goods_id) references goods(id), '\
  'order_id int, '\
  'foreign key(order_id) references orders(id), '\
  'quantity int)'
))

for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
