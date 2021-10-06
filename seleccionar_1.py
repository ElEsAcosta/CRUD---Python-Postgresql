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

#Solicitar cedula
print('---------------------------------------------------')
cedula_us=input('Ingrese el cedula del usuario a mostrar: ')

#Sentencia SQL
sql='SELECT * FROM usuario WHERE cedula_us=%s'

#Metodo execute
cursor.execute(sql,(cedula_us,))

#mostrar resultado
registro=cursor.fetchone()

#mostrar en consola
print('---------------------------------')
print(registro)
print('---------------------------------')
import main

#cerrar conexiones
cursor.close()
conexion.close()