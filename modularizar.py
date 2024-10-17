from funcion_mensaje_menu import *
from funcion_ingresar_datos_alumnos import *
from funcion_guardar_datos_alumnos import *
while True:
    menu_opciones=input(mensaje_menu())

    if menu_opciones.lower()=="n":
        print("saliendo del Sistema")
        break
    elif menu_opciones.lower()=="s":
        ingresar_datos_alumnos()  
    else:
        print("Opcion erronea")

print(lista_alumnos)

#tarea hecha