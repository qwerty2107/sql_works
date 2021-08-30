import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('update goods'\
'set price = price + 100'\
'where id not in'\
'('\
  'select goods_id from order_items'\
  'where order_id in'\
  '('\
    'select id from orders'\
    'where month(date) = 07'\
  ')'\
')'
))

for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
