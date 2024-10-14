#tarea: 
"""
- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio
"""
#Esta es una "programacion funcional"
lista_alumnos=[]
def mensaje_menu():
    menu_opciones="""
        .............Bienvenido al sistema!.............
        .................. Registrese ..................
                        elije lo que deseas hacer: 
        1. Escribe [s] si deseas registrar un alumno
        2. Escribe [n] si deseas salir del programa
        Escribe tu respuesta: """
    return menu_opciones

def ingresar_datos_alumnos():
    id=len(lista_alumnos)+1
    cui=int(input("Ingrese el numero de su dni: "))
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    numero_celular=int(input("Ingrese su numero de celular: "))
    programa_estudio=input("Ingrese programa de estudio: ")
    ciclo_academico=input("Ingrese su ciclo academico: ")
    email=input("Ingrese su correo electronico: ")
    guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno={
            "id":id,
            "cui":cui,
            "nombre":nombre,
            "apellido":apellido,
            "numero_celular":numero_celular,
            "programa_estudio":programa_estudio,
            "ciclo_academico":ciclo_academico,
            "email":email
            }
    lista_alumnos.append(alumno)

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


#la tarea que hice  
# a = 0
# while a < 20:
#     nombre=input("Ingrese nombre completo: ")
#     edad=int(input("Ingrese su edad: "))
#     matricula=int(input("Ingrese id matricula: "))
#     programa=input("Ingrese programa de estudio: ")
#     a = a + 1
# else:
#      print("limite de estudiantes")
