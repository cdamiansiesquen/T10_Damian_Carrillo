import libreria

def anadirDatos():
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    apellido=libreria.pedir_apellido("Ingresar apellido:")
    dni=libreria.pedir_dni("Ingresar DNI:")
    contenido=" DNI:" + dni + "-" + "Nombre:" + str(nombre) + "-" + "Apellido:" + str(apellido) + "\n"
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
    print("1. Agregar Datos personales")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirDatos()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
