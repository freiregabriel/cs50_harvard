import sqlite3
import json

def execute(query, table):
    c.execute(query, (table,))
    return c.fetchall()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


connection = sqlite3.connect('app.db')
connection.row_factory = dict_factory
c = connection.cursor()

# rows = execute('SELECT * FROM registrants')
# # print(rows)
# for row in rows:
#     # print(row)
#     print(f"{row['name']} is registered")

# execute_script("""
#     INSERT INTO registrants (id, name, dorm) VALUES(3, 'Gabriel', 'Any dorm');
#     INSERT INTO registrants (id, name, dorm) VALUES(4, 'John', 'Any dorm2');
#     INSERT INTO registrants (id, name, dorm) VALUES(5, 'Chris', 'Any dorm3');
#     """)


# connection.commit()
def get_all(table):
    rows = execute('SELECT * FROM ?', table)
    return rows
connection.close()