from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='127.0.0.1', user='root', password='Senha123@', database='Fist_db')
mycursor=mydb.cursor()

mycursor.execute('select * from Clientes')

result=mycursor.fetchall()
for i in result:
    print(i)