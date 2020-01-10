import libreria

def anadirDia():
    dia=libreria.pedir_dia("Ingresar dia:")
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    region=libreria.pedir_region("Ingresar la region:")
    contenido=" Dia:" + dia + "-" + "Nombre:" + str(nombre) + "-" + "region:" + str(region) + "\n"
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
    print("1. Agregar fecha")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirDia()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
