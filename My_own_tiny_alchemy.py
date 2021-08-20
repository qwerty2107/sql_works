import mysql.connector


database_name = 'example'

example = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database= database_name)

tables = []


cursor = example.cursor()


class sql_table():
    def __init__(self, table_name, **columns):
        # columns:   column_name=('data type', foreign_key (or None))
        self.table_name = table_name
        self.columns = columns
        tables.append(self)
    def create(self):
        table_creation = 'create table ' + self.table_name + ' (id int primary key auto_increment'
        for n in self.columns:
            table_creation += ', ' + n + ' ' + self.columns[n][0]
            if self.columns[n][1] != None:
                table_creation += ', foreign key (' + n + ') references ' + self.columns[n][1]
        table_creation += ')'
        print((table_creation))
        cursor.execute((table_creation))
    def add_values(self, used_columns, *new_values):
        # used_columns = (column1, column2, ... )
        # new_values = (column1_value, column2_value, ... )
        if type(used_columns) is not tuple:
            used_columns = (used_columns,)
        if type(new_values) is not tuple:
            new_values = (new_values,)
        values_insertion = 'insert ' + self.table_name + '('
        for n in used_columns:
            values_insertion += n + ', '
        values_insertion = values_insertion[:-2]
        values_insertion += ') values '
        for n in new_values:
            if type(n) is not tuple:
                n = (n,)
            values_insertion += '('
            for m in n:
                if type(m) is int:
                    m = str(m)
                else:
                    m = '"' + m + '"'
                values_insertion += m + ', '
            values_insertion = values_insertion[:-2]
            values_insertion += '), '
        values_insertion = values_insertion[:-2]
        print((values_insertion))
        cursor.execute((values_insertion))
        example.commit()
    def select_column(self, column_name):
        result = []
        cursor.execute(('select ' + column_name + ' from ' + self.table_name))
        for n in cursor:
            result.append(n)
        return result


def get_tables():
    table_columns = {}
    cursor.execute(('select table_name, column_name, data_type from information_schema.columns where table_schema = "'
    + database_name + '"'))
    for n in cursor:
        if n[0] not in table_columns.keys():
            table_columns[n[0]] = {}
            table_columns[n[0]][n[1]] = (n[2], None)
        else:
            table_columns[n[0]][n[1]] = (n[2], None)
    cursor.execute(('select table_name, column_name, referenced_table_name, referenced_column_name ' +
    'from information_schema.key_column_usage where constraint_schema = "' + database_name +
    '" and referenced_table_schema is not null and referenced_table_name is not null and ' +
    'referenced_column_name is not null'))
    for n in cursor:
        table_columns[n[0]][n[1]] = (table_columns[n[0]][n[1]][0], n[2] + '(' + n[3] + ')')
    for n in table_columns:
        sql_table(n, **table_columns[n])

def show_tables():
    for n in tables:
        print('Table:  ' + n.table_name)
        for m in n.columns:
            print(m)
        print()

def join(*selected_tables):
    pass

def general_input():
    pass






#goods = sql_table('goods', name=('varchar(50)',None), price=('int',None))
#goods.create()
#goods.add_values(('name','price'),('Expensive box',200),('Affordable box',100),('Cheap box',50))

#orders = sql_table('orders', date=('date',None))
#orders.create()
#orders.add_values(('date'), ('2021-07-25'), ('2021-07-25'), ('2021-07-30'), ('2021-08-01'))

#order_items = sql_table('order_items', goods_id=('int','goods(id)'), order_id=('int','orders(id)'), quantity=('int',None))
#order_items.create()
#order_items.add_values(('order_id','goods_id','quantity'), (1,1,2), (1,2,4), (2,3,100), (3,2,15), (3,3,20), (4,1,3))


get_tables()
show_tables()
tables[0].select_all()

cursor.close()
example.close()

input()


# Interface
#
#
# from tkinter import *
# window = Tk()
# window.geometry('1200x800+200+100')
# window.title('SQL server overview')
# Grid.columnconfigure(window, 0, weight=1)
# Grid.rowconfigure(window, 0, weight=1)
#
#
# class Window_Frame():
#     def __init__(self):
#         self.frame = Frame(window)
#     def show_widgets(self):
#         pass
#     def show(self):
#         self.frame.grid(sticky='nswe')
#         self.show_widgets()
# window.mainloop()
