import libreria

def anadirRest():
    restaurant=libreria.pedir_lugar("Ingresar lugar de restaurant(braza roja, marakos, norkys):" )
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    plato=libreria.pedir_plato("Ingresar pedido(ceviche, arroz con pato, causa):")
    contenido=" restaurant:" + restaurant + "-" + "Nombre:" + str(nombre) + "-" + "plato:" + str(plato) + "\n"
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
    print("1. Agregar Lugar de comida y pedido")
    print("2. Ver informacion")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirRest()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
