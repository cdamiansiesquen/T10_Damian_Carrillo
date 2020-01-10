
def validar_entero(n):
    if(isinstance(n,int)):
        return True
    else:
        return False

def pedir_entero(en):
    ent=""
    while(validar_entero(ent) == False):
        ent=input(en)
    #fin_while
    return ent

def validar_rango(n, ri, rf):
    if( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while(validar_rango(n, ri, rf) == False):
        n=input(msg)
        if(n.isdigit()== True):
            n= int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_dni(d):
    if (len(d) == 8 ):
         if ( d.isdigit() == True ):
             return True
         else:
             return False
     #fin_if
    else:
         return False
#fin_pedir_año

def pedir_dni(dn):
    dni=""
    while(validar_dni(dni) == False):
        dni=input(dn)
    #fin_while
    return dni


def validar_nombre(x):
     if (isinstance(x, str)):
         if(len(x) > 4):
             return True
         else:
             return False
     else:
         return False

def pedir_nombre(nom):
    nombre=""
    while(validar_nombre(nombre) == False):
        nombre=input(nom)
    #fin_while
    return nombre

def validar_apellido(e):
     if (isinstance(e, str)):
         if(len(e) > 4):
             return True
         else:
             return False
     else:
         return False

def pedir_apellido(ape):
    apellido=""
    while(validar_apellido(apellido) == False):
        apellido=input(ape)
    #fin_while
    return apellido

def validar_region(r):
    if(isinstance(r, str)):
        if(len(r) > 3):
            return True
        else:
            return False
    else:
        return False

def pedir_region(reg):
    region=""
    while(validar_region(region) == False):
         region=input(reg)
    #fin_while
    return region

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def pedir_nota(msg, ri, rf):
    n=""
    while(validar_rango(n ,ri ,rf) == False):
        n=input(msg)
        if(n.isdigit()== True):
            n=int(n)
    #fin_while
    return n

def validar_ano(a):
        if(len(a) == 4):
            return True
        else:
            return False

def pedir_ano(ano):
    anno=""
    while(validar_ano(ano) == False):
         anno=input(ano)
    #fin_while
    return anno

def validar_pais(p):
    if(isinstance(p, str)):
        if(len(p) > 3):
            return True
        else:
            return False
    else:
        return False

def pedir_pais(ps):
    pais=""
    while(validar_pais(pais) == False):
         pais=input(ps)
    #fin_while
    return pais

def validar_distrito(t):
    if(isinstance(t, str)):
        if(len(t) > 4):
            return True
        else:
            return False
    else:
        return False

def pedir_distrito(dis):
    distrito=""
    while(validar_distrito(distrito) == False):
         distrito=input(dis)
    #fin_while
    return distrito


def validar_dia(di):
    if(isinstance(di, str)):
        if(len(di) >=4):
            return True
            if(di=="lunes" or di=="martes" or di=="miercoles" or di=="jueves" or di=="viernes" or di=="sabado" or di=="domingo"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def pedir_dia(msg):
    di=""
    while(validar_dia(di) == False):
        di=input(msg)
    #fin_while
    return di
#fin_pedir_dia


def validar_sexo(sexo):
    if(isinstance(sexo, str)):
        if(len(sexo) == 9 or len(sexo) == 8):
            return True
            if(sexo == "Mascuclino" or sexo ==  "Femenino"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_sexo(msg):
    sexo= ""
    while( validar_sexo(sexo)== False):
        sexo=input(msg)
    #fin_while
    return sexo
#fin_pedir_sexo


def validar_planeta(plan):
    if(isinstance(plan, str)):
        if(plan == "Mercucrio" or plan == "Venus" or plan == "Tierra" or plan == "Marte" or plan == "Jupiter" or plan == "Saturno" or plan == "Urano" or plan == "Neptuno"):
            return True
        else:
            return False
    else:
        return False

def pedir_planeta(pl):
    planeta= ""
    while( validar_planeta(planeta)== False):
        planeta=input(pl)
    #fin_while
    return planeta
#fin_pedir_planeta

def validar_continente(conti):
    if(isinstance(conti, str)):
        if(conti == "America" or conti == "Europa" or conti == "Africa" or conti == "Asia" or conti == "Oceania"):
            return True
        else:
            return False
    else:
        return False

def pedir_continente(con):
    continente= ""
    while(validar_continente(continente)== False):
        continente=input(con)
    #fin_while
    return continente
#fin_pedir_continente


def validar_plato(pla):
    if(isinstance(pla, str)):
        if(pla == "arooz con pollo" or pla ==  "ceviche" or pla == "Causa"):
            return True

        else:
            return False
    else:
        return False

def pedir_plato(msg):
    plato= ""
    while( validar_plato(plato)== False):
        plato=input(msg)
    #fin_while
    return plato
#fin_pedir_sexo

def validar_lugar(lug):
    if(isinstance(lug, str)):
        if(lug == "braza roja" or lug ==  "marakos" or lug == "norkys"):
            return True
        else:
            return False
    else:
        return False

def pedir_lugar(msg):
    lugar= ""
    while( validar_lugar(lugar)== False):
        lugar=input(msg)
    #fin_while
    return lugar
#fin_pedir_sexo
