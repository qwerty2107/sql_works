import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('select orders.id, orders.date, sum(quantity*price) from orders '\
'left join order_items on orders.id = order_items.order_id '\
'left join goods on order_items.goods_id = goods.id '\
'group by orders.id, orders.date'))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
