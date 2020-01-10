import libreria

def anadirPedido():
    nombre=libreria.pedir_nombre("Ingresar nombre:")
    platos=libreria.pedir_plato("Ingresar platos(ceviche,arroz con pato, causa):")
    contenido=" nombre:" + nombre  + "platos:" + str(platos) + "\n"
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
    print("1. Agregar pedido")
    print("2. Ver pedido")
    print("3. SALIR")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion",1, 3)

    if(opc == 1):
        anadirPedido()

    if(opc == 2):
        verDatos()

#fin_menu
print("fin del programa")
