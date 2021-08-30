import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('select * from orders '
'left join '
'( '
  'select order_id,sum(price*quantity) '
  'from order_items '
  'inner join goods '
  'on goods.id = order_items.goods_id '
  'group by order_id '
') as t1 '
'on orders.id = t1.order_id'))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
