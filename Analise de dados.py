import pandas.io.sql as pd
import sqlite3
import pyodbc


### Cria coneçao com o banco de dados principal ###

##;UID=username;PWD=password

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-4B7F9M8\SQLEXPRESS;DATABASE=essavai')
cursor = cnxn.cursor()
sql = ('''
select * from cidade

''')

### Salva o resultado SQL em UM Data Frame e fecha a conexao com o banco principal ###
Data = pd.read_sql_query(sql, cnxn)
cnxn.close()


### Cria um novo banco para os dados coletados do banco principal ###
with sqlite3.connect("Data.db") as con:
    #### nome da tabela em 'Dados' ###
    Data.to_sql('Dados',con)