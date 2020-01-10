import libreria

def anadirPais():
    pais=libreria.pedir_pais("Ingresar DNI:")
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    nombre_continente=libreria.pedir_continente("Ingresar nombre del contiente:")
    contenido=" pais:" + pais + "-" + "Nombre:" + str(nombre) + "-" + "Pais:" + str(nombre_continente) + "\n"
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
    print("1. Agregar pais")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirPais()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
