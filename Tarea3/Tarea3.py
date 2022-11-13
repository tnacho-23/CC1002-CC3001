######### ----- Tarea 3 ----- #########
## Importación de modulos ##
import estructura

## Creacion de estructuras mutables ##

# objeto: Nombre(str) Tipo(str) Cantidad(int) Felicidad(int)
#           Estudio(int) Materia(str)
estructura.mutable("objeto","Nombre Tipo Cantidad Felicidad Estudio Materia")

## Funciones Auxiliares ##
# IgualObjeto: objeto objeto -> bool
# Indica si dos objetos tienen los mismos
# parametros. Esta función será utilizada para
# hacer los test de la función leerInventario(Nombre)
# Ejemplo:  IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
#           objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")) -> True
def IgualObjeto(Obj1, Obj2):
    return ((Obj1.Nombre == Obj2.Nombre) and
            (Obj1.Tipo == Obj2.Tipo) and
            (Obj1.Cantidad == Obj2.Cantidad) and
            (Obj1.Felicidad == Obj2.Felicidad) and
            (Obj1.Estudio == Obj2.Estudio) and
            (Obj1.Materia == Obj2.Materia))
# Test
assert(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")))
assert not(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Fisica","Libro",1,-7,25,"Fisica")))
assert not(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Codigo Secreto","Juego de Mesa",0,30,-7,"No aplica")))

        
# leerInventario: string -> lista
# Lee un archivo txt entregando una lista
# de objetos correspondientes a cada linea
# del archivo de texto.
# Condiciones: Para leer el archivo txt es
# necesario que este se encuentre en la misma
# carpeta que este archivo.py
# Recordar que 
# Ejemplo: 
def leerInventario(Nombre):
    inventario = [] # Lista vacia donde se guardarán los objetos
    inv = open(Nombre, 'r') # Se abre el archivo en modo lectura
    for linea in inv: # Se lee cada linea del archivo
        Obj = linea.split(";") # Separa cada string en una lista
        # tomando como separador ;
        # Luego crea el objeto tomando cada valor de la lista
        # anteriormente creada
        Obj = objeto(Obj[0], Obj[1], int(Obj[2]),
                     int(Obj[3]), int(Obj[4]), Obj[5][:-1])
        # Para el último valor (Obj[5]), el string termina con
        # un salto de linea \n , por lo que para ignorar
        # ese salto de linea se toman todos los caracteres
        # de ese último string menos el último
        inventario.append(Obj) # Se guarda el objeto en la lista
    return inventario
# Test
Inv = leerInventario("Inventario.txt")
Obj6 = objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")
Obj33 = objeto("Fisica","Libro",1,-7,25,"Fisica")
Obj19 = objeto("Essential Cell Biology","Libro",1,-7,20,"Biologia")
assert(IgualObjeto(Inv[6],Obj6))
assert(IgualObjeto(Inv[33],Obj33))
assert(IgualObjeto(Inv[19],Obj19))
