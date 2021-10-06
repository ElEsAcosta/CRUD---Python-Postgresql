# importacion del modulo de conexion a postgres
import psycopg2

# Conexion BD
conexion=psycopg2.connect(user='postgres', 
                          password='1999wildfire',    
                          host='127.0.0.1',
                          port='5432',
                          database='db_usuarios')


# Utilizar cursor
cursor=conexion.cursor()

#Sentencia SQL
sql='SELECT * FROM usuario'

#Metodo execute
cursor.execute(sql)

#mostrar resultado
registro=cursor.fetchall()

#mostrar en consola
for fila in registro:
    print(fila)
print('---------------------------------')
import main

#cerrar conexiones
cursor.close()
conexion.close()