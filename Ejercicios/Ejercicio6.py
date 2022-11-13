from estructura import *
from lista import *
#Estructura que sirve para crear árboles
#donde valor será el valor central
#izq y der serán las ramas a la izquierda
#y la derecha del valor central, respectivamente
crear('AB', 'valor izq der')
#Ejemplos:
Vacio=AB(None,None,None)
Hoja1=AB(2,None,None)
Hoja2=AB(4,None,None)
Hoja3=AB(5,None,None)
Ramita=AB(8,Hoja1,Hoja2)
Rama1=AB(7,Ramita,None)
Rama2=AB(2,Hoja3,None)
Raiz=AB(1,Rama1,Rama2)
#-----------------------------------------------------
#altura: AB -> int
#Recibe un árbol y retorna la altura de este
#Ej: altura(Raiz)->4
#    altura(Vacio) -> 0
#    altura(Rama2) -> 2
def altura(árbol):
    if árbol==None:
        return 0
    elif árbol==Vacio:
        return 0
    else:
        return max(altura(árbol.izq),altura(árbol.der))+1
#Test
assert(altura(Raiz)==4)
assert(altura(Vacio) == 0)
assert(altura(Rama2) == 2)

#----------------------------------------------------
#contador: AB -> int
#Recibe un árbol y retorna
#La suma de los valores de todos los
#nodos del árbol.
#Ej.  contador(Vacio) -> 0
#     contador(Raiz) -> 29
#     contador(Ramita) -> 14
def contador(árbol):
    if árbol == None:
        return 0
    elif árbol == Vacio:
        return 0
    else:
        return árbol.valor+contador(árbol.izq)+ contador(árbol.der)

#Test
assert(contador(Vacio) == 0)
assert(contador(Raiz) == 29)
assert(contador(Ramita)==14)
