#tarea especial
# """
# - registrar alumnos.
#   //Historias de usuarios
#   [x] yo como registrador deseo poder almacenar sus datos
#   pernonales para tener un correcto manejo de la informacion.
#      // Lista de aceptacion:
#      [x] cui
#      [x] nombre
#      [x] apellido
#      [x] programa_estudio
#      [x] ciclo
#      [x] nacionalidad
#      [x] fecha_nacimiento
#      [x] numero_celular
#      [x] email
#     [ ] YO COMO REGISTRADOR deseo registrar de manera obligatoria
#     el dni y el nomre del alumno para tener esos datos de manera obligatoria.
#      // Lista de aceptacion:
#      [ ] cui
#      [ ] nombre
#     [ ] yo como registrado deseo que se verifique si el correo es el correcto
#     para evitar poner datos erroneos.
#      // Lista de aceptacion:
#      [x] email:verificar que tenga la estructura correcta de un email @
#      y el dominio (.com)
#     [ ] yo como regstrador deseo que se validen los datos para tener un mayor
#     control de la informacion que se almacena.
#      // Lista de aceptacion:
#      [x] nombre: tenga como maximo 8 caracteres y solo sea texto.
#      [x] apellido: tenga como maximo 25 solo caracteres.
#      [x] cui: solo numeros y debe tener 8 digitos no mas ni menos.
#      [x] numero_celular: debe ser numero y tener 9 digitos.
     
# - generar fichas de matricula
# - mostrar la lista de todos los matriculados
# - filtrar matriculados por programa de estudio
# """
# #metodo original
# lista_alumnos=[]

# while True:
#     opcion:str=input("""elije lo que deseas hacer: 
#                  escribe [s] si deseas registrar un alumno
#                  escribe [n] si deseas salir del programa
#                  escrive tu respuesta: """)
#     if opcion.lower()=="n":
#         print("Saliedo del sistema ......")
#     if opcion.lower()=="s":
#         print("realice lo siguiente:")
#         break
    
#     """ Refactorizar
#        tengo codigo repetido, tengo dos while que hacen lo
#        mismo busca una manera de hacer el codigo mas pequeño
#     """
#     # verificar cui de dni
# while True:
#     cui:int=input("ingresa su nuero de dni: ")
#     if cui !="":
#         break
#     print("es obligatorio el ingresar un numero de dni")
#     # verifica nombre del anumno
# while True:
#     nombre:str=input("ingresar el nombre del alumno: ")
#     if nombre=="":
#         print("es obligatorio el ingresar nombre del alumno: ")
#     else:
#         break

# apellido:str=input("Ingrese el apellido del alumno: ")
# programa_estudio:str=input("Ingresa el programa de estudio: ")
# ciclo:str=input("Ingrese el ciclo academico: ")
# nacionalidad:str=input("Ingrese su nacionalidad: ")
# fecha_nacimiento:str=input("Ingresa tu fecha de nacimiento: ")
# numero_celular:int=input("Ingresa el numero de celular: ")
# email:str=input("Ingresa el email: ")

# alumno:dict={
#     "cui":cui,
#     "nombre":nombre,
#     "apellido":apellido,
#     "programa_estudio":programa_estudio,
#     "ciclo_academico":ciclo,
#     "nacionalidad":nacionalidad,
#     "fecha_nacimiento":fecha_nacimiento,
#     "numero_celular":numero_celular,
#     "email":email
# }
# lista_alumnos.append(alumno)

# print(lista_alumnos)

