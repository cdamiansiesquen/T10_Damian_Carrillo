import libreria

def anadirDni():
    dni=libreria.pedir_dni("Ingresar DNI:")
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    nombre_pais=libreria.pedir_pais("Ingresar nombre del pais:")
    contenido=" DNI:" + dni + "-" + "Nombre:" + str(nombre) + "-" + "Pais:" + str(nombre_pais) + "\n"
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
    print("1. Agregar informacion")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirDni()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
