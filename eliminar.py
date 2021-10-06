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

#Sentencia 
sql='DELETE FROM usuario WHERE cedula_us=%s'

#Solicitar dato al usuario
print('---------------------------------------------------')
cedula_us=input('Ingrese la cedula del usuario a eliminar: ')

#metodo execute
cursor.execute(sql,(cedula_us,))

#guardar cambios
conexion.commit()

#Noti usuario
print('---------------------------------')
print('Registro eliminado con exito')
import main

#Cerrar conexion
cursor.close()
conexion.close()