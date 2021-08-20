import mysql.connector
database_name = 'example'
example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)
cursor = example.cursor()
cursor.execute(('Your sql query'))
for n in cursor:
    print(n)
cursor.close()
example.commit()
example.close()
