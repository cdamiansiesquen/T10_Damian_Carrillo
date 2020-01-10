import libreria

def anadirUbicacion():
    pais=libreria.pedir_pais("Ingresar pais:")
    continente=libreria.pedir_continente("Ingresar continente:")
    planeta=libreria.pedir_planeta("Ingresar planeta:")
    contenido=" pais:" + pais + "-" + "continente:" + str(continete) + "-" + "planeta:" + str(planeta) + "\n"
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
    print("1. Agregar ubicacion")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirUbicacion()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
