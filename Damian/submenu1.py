import libreria


def documentacion1():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("NOMBRE:")
    edad=libreria.pedir_numero("EDAD:", 1, 50)
    contenido = dni + "-" + str(nombre) + "-" + str(edad) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos Guardados")

def documentacion2():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("NOMBRE:")
    edad=libreria.pedir_numero("EDAD:", 51, 90)
    contenido = dni + "-" + str(nombre) + "-" + str(edad) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos Guardados")

def verDatos():
    datos = libreria.obtener_datos("info.txt")
    if(datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

def menores_de_edad():
    opc=0
    max=3
    while(opc != max):
        print("########## Informacion ###########")
        print("1. Documentacion menores de 50 años de edad")
        print("2. Ver informacion")
        print("3. SALIR")
        print("###########################")
        opc=libreria.pedir_numero("ingrese opcion:", 1, 3)
        if(opc==1):
            documentacion1()
        if(opc==2):
            verDatos()

def mayores_edad():
    opc=0
    max=3
    while(opc != max):
        print("########## Informacion 2  ###########")
        print("1. Documentacion mmayores de 50 años de edad")
        print("2. Ver informacion")
        print("3. SALIR")
        print("###########################")
        opc=libreria.pedir_numero("ingrese subopcion:", 1, 3)
        if(opc==1):
            documentacion2()
        if(opc==2):
            verDatos()

opc=0
max=3
while(opc != max):
    print("########## MENU ###########")
    print("1. menores de edad")
    print("2. mayores de edad")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 3)

    if(opc==1):
        menores_de_edad()
    if(opc==2):
        mayores_edad()

#fin
print("fin del programa")
