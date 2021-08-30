import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('update order_items' +
'set quantity = quantity + 1' +
'where goods_id in' +
'(' +
 'select goods_id' +
 'from order_items' +
 'where order_id in' +
  '(' +
    'select orders.id' +
    'from orders' +
    'where month(orders.date) = month('2021-07-01')' +
   ')' +
')'))

for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
