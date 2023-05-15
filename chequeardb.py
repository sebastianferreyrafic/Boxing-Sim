import sqlite3
#from class_fight import *

# Conexión a la base de datos
conn = sqlite3.connect('boxeodb.db')
cursor = conn.cursor()
cursor.execute("select * from boxeadores")
for d in cursor:
    print(d)
cursor.execute("select * from peleas")
for d in cursor:
    print(d)
conn.close()

"""


# Conectarse a la base de datos
conn = sqlite3.connect("boxeodb.db")
c = conn.cursor()

# Ejecutar una consulta para obtener los datos
c.execute("SELECT * FROM peleas")

# Obtener los nombres de las columnas
column_names = [column[0] for column in c.description]

# Obtener todas las filas de los resultados
rows = c.fetchall()

# Imprimir los nombres de las columnas
print(column_names)

# Imprimir los datos de cada fila
for row in rows:
    print(row)

# Cerrar la conexión a la base de datos
conn.close()"""