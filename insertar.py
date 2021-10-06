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

#crear sentencia sql
sql='INSERT INTO usuario (cedula_us,nombre_us,apellido_us) VALUES(%s,%s,%s)'

#Solicitud de datos
print('---------------------------------------------------')
cedula=input('Ingrese la cedula del usuario: ')
nombre=input('Ingrese el nombre del usuario: ')
apellido=input('Ingrese el apellido del usuario: ')

#recoleccion de datos
datos=(cedula,nombre,apellido)

#Metodo execute
cursor.execute(sql,datos)

#Guardar registro
conexion.commit()

#mostrar mensaje
print('---------------------------------')
print('Registro exitoso.')
import main

#Cerrando conexion
cursor.close()
conexion.close()