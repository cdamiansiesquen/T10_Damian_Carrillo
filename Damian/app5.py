import libreria

def anadirLugar():
    distrito=libreria.pedir_distrito("Ingresar distrito:")
    region=libreria.pedir_region("Ingresar region:")
    pais=libreria.pedir_pais("Ingresar pais:")
    contenido=" Distrito:" + distrito + "-" + "region:" + str(region) + "-" + "Pais:" + str(pais) + "\n"
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
    print("1. Agregar lugar")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirLugar()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
