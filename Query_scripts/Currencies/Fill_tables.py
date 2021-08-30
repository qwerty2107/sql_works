import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('insert currencies(code)' +
'values' +
"('USD')," +
"('EUR')," +
"('CNY')," +
"('JPY')," +
"('ABC');" +
'insert ratios(date, currency_id, value)' +
'values' +
"('2021-07-25',1,73.71)," +
"('2021-07-26',1,73.72)," +
"('2021-07-27',1,73.74)," +
"('2021-07-28',1,73.47)," +
"('2021-07-29',1,73.19)," +
"('2021-07-30',1,73.15)," +
"('2021-07-25',2,86.60)," +
"('2021-07-28',2,87.03)," +
"('2021-07-30',2,86.81)," +
"('2021-07-25',5,10.52)," +
"('2021-07-26',5,10.52)," +
"('2021-07-29',5,10.68)"))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
