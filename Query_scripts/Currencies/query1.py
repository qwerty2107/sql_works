import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
currency_code = 'ABC'
date = '2021-07-28'
cursor.execute(('select currencies.code, ratios.date, ratios.value from currencies'\
'right join ratios'\
'on currencies.id = ratios.currency_id'\
f"where currencies.code = 'ABC' and ratios.date in"\
'('\
  'select max(date) from currencies'\
  'right join ratios'\
  'on currencies.id = ratios.currency_id'\
  f"where currencies.code = {currency_code} and ratios.date<={date}"\
')'))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
