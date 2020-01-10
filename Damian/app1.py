import libreria

def anadirSexo():
    sexo=libreria.pedir_sexo("Ingresar sexo:")
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    nombre_distrito=libreria.pedir_distrito("Ingresar nombre del distrito:")
    contenido=sexo + "-" + str(nombre) + "-" + str(nombre_distrito) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos Guardados")

def verDatos():
    datos = libreria.obtener_datos("info.txt")
    if(datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("########## MENU ###########")
    print("1. Agregar sexo")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirSexo()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
