menu = """
BIENVENIDO AL SISTEMA DE USUARIOS
---------------------------------------------------
DIGITE SU OPCION:
1) Ingresar usuario.
2) Actualizar usuario.
3) Buscar usuario.
4) Eliminar usuario.
5) Mostrar todos los usarios registrados.
6) Salir.
---------------------------------------------------
"""
print(menu)

op=int(input("Opcion: "))

if op == 1:
    import insertar
elif op == 2:
    import actualizar
elif op == 3:
    import seleccionar_1
elif op == 4:
    import eliminar
elif op == 5:
    import selecccionar_todes
elif op == 6:
    quit()
else:
    print('----------------------')
    print("Opcion erronea.")
    print('----------------------')
    import main
import main


