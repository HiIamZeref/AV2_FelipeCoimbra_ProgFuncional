import mysql.connector
from pprint import pprint

db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'password'
)

CURSOR = db.cursor()

executeCommand = lambda command: CURSOR.execute(command)

#DATABASE
createDatabase = lambda database_name: executeCommand(f"CREATE DATABASE {database_name};")
useDatabase = lambda database_name: executeCommand(f"USE {database_name};")


#TABLE
createTable = lambda table_name, attributes: executeCommand(f"CREATE TABLE {table_name}({attributes});")
dropTable = lambda table_name: executeCommand(f"DROP TABLE {table_name};")


insertTable = lambda table_name, attributes, values: executeCommand(f"INSERT INTO {table_name}({attributes}) VALUES ({values});")
selectTable = lambda table_name: executeCommand(f"SELECT * from {table_name};")
removeTable = lambda table_name, id: executeCommand(f"DELETE FROM {table_name} WHERE id={id};")

database_name = "funcional"

#CRIANDO DATABASE
createDatabase(database_name)
useDatabase(database_name)

#CRIANDO TABLES
createTable("USUARIOS", "id int not null, nome varchar(100) not null, console varchar(100) not null")
createTable("JOGOS", "id int not null, nome varchar(100) not null, data_lancamento varchar(100) not null")

insertTable("USUARIOS", "id, nome, console", "01, 'felipe', 'PC'")
selectTable("USUARIOS")

consulta = CURSOR.fetchall()
print("Consulta: ")
show = [pprint(row) for row in consulta]

removeTable("USUARIOS", "01")

insertTable("JOGOS", "id, nome, data_lancamento", "01, 'spiderman 2', '20/10/2023'")
selectTable("JOGOS")

consulta = CURSOR.fetchall()
print("Consulta: ")
show = [pprint(row) for row in consulta]

CURSOR.close()
db.close()