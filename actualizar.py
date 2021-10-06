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

# crear sentencia sql
sql='UPDATE usuario SET nombre_us=%s,apellido_us=%s WHERE cedula_us=%s'

# Consulta de datos a usuario
print('-----------------------------------------')
cedula_us=input('Ingrese la cedula de la persona a editar: ')
print('-----------------------------------------')
nombre_us=input('Ingrese nombre: ')
apellido_us=input('Ingrese apellido: ')

# Recoleccion de datos
datos=(nombre_us,apellido_us,cedula_us)

# utilizar el metodo execute
cursor.execute(sql,datos)

# Guardar mod
conexion.commit()

#Mostrar mensaje al usuario
print('---------------------------------')
print('Actualizaciòn exitosa.')
import main

#cerrar conexiones
cursor.close()
conexion.close()



