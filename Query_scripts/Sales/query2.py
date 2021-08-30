import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('select avg(price*quantity) from order_items'\
'left join (orders, goods)'\
'on (orders.id = order_items.order_id'\
'and goods.id = order_items.goods_id')))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
