from estructura import *
from lista import *
from math import *
import random
#-------------------------------------------------------------
#Estructura para los peces
#pez: tipo (str) peso (int) puntaje(int)
#estructura que recibe un tipo de pez, venenoso o delicioso,
#su peso, un número aleatorio entre 1 y 5, y el puntaje,
#si el pescado es delicioso el puntaje es entre
#5 y 50, si es venenoso está entre -50 y -5.
#Ej. pez('delicioso',3,10)
#    pez('venenoso',2,-25)
crear('pez', 'tipo peso puntaje')

#-----------------------------------------------------------
#generarPeces: int -> lista
#recibe un número entero y
#retorna una lista de K elementos, donde cada elemento de la
#lista puede ser None (30% de probabilidad), un pez delicioso
#(35% de probabilidad) o un pez venenoso (35% de probabilidad).
#Ej:generarPeces(0) -> listaVacia
#   generarPeces(2) -> lista(valor=None, siguiente=lista 
#(valor=pez(tipo='delicioso', peso=4, puntaje=28), siguiente=None))
def generarPeces(k):
    if k==0:
        return None
    else:
        r=random.uniform(1,100)
        if r<=30:
            return lista(None,generarPeces(k-1))
            
        elif r<=65:
            delicioso=pez('delicioso',random.randint(1,5),random.randint(5,50))
            return lista(delicioso,generarPeces(k-1))
            
        else:
            venenoso=pez('venenoso',random.randint(1,5),random.randint(-50,-5))
            return lista(venenoso,generarPeces(k-1))
        


#Test:
prueba=generarPeces(4)
prueba1=generarPeces(0)
assert type(prueba)==lista and type(prueba)==lista
assert prueba1==listaVacia
assert cabeza(prueba)==None or cabeza(prueba).tipo==('delicioso') or cabeza(prueba).tipo==('venenoso')
#-----------------------------------------------------------
#generarPez
#entrega un pez con 50% de probabilidad
#de ser delicioso y 50% de ser venenoso
#Ej: generarPez() -> pez('venenoso',5,-7)
#    generarPez() -> pez('delicioso,2,25)
def generarPez():
    r=random.random()
    if r<=0.5:
        return pez('delicioso',random.randint(1,5),random.randint(5,50))
    else:
        return pez('venenoso',random.randint(1,5),random.randint(-50,-5))
#Test
pezPrueba=generarPez() 
assert(pezPrueba.tipo == 'delicioso' or pezPrueba.tipo == 'venenoso')
assert(pezPrueba.peso>=1 and pezPrueba.peso<=5)
assert (pezPrueba.puntaje >= -50 and pezPrueba.puntaje<=50 and
        not(pezPrueba.puntaje < 5 and pezPrueba.puntaje > -5))

#----------------------------------------------------------------
#printearLista: lista -> str
#Recibe una lista y printea cada elemento de esta
#Ej: sea a=lista(1,lista(2,None))
#   printearLista(a) -> 1
#                       2
#                     None

def printearLista(Lista):
    if Lista == listaVacia:
        return print(None)
    else:
        print(cabeza(Lista))
        return printearLista(cola(Lista))
#Test:
#No aplica

#---------------------------------------------------------------
#sacarDeLista: lista int -> valor lista
#Recibe una lista L y un entero k, esta
#función entrega el elemento k-esimo de la lista
#Ej: sea a=lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))
#   sacarDeLista(a,1)-> 1
#   sacarDeLista(a,4)-> 4
#   sacarDeLista(a,6) -> None
def sacarDeLista(lista,k):
    if k==1:
        return cabeza(lista)
    else:
        k-=1
        return sacarDeLista(cola(lista),k)
#Test:
a=lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))
assert(sacarDeLista(a,1)==1)
assert(sacarDeLista(a,4)==4)
assert(sacarDeLista(a,6)==None)
#--------------------------------------------------------------
#agregar: lista x -> lista
# retorna una lista con todos los elementos
#de la lista entregada más el elemento x
#Ej. agregar(lista(1,lista(2,None)),3) -> lista(3,lista(1,lista(2,None)))
def agregar(L,x):
    return lista(x,L)
#Test:
a=lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))
assert(agregar(a,0)== lista(0,lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))))
assert(agregar(a,None)== lista(None,lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))))
assert(agregar(a,'buen día grupo')== lista('buen día grupo',lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))))
#----------------------------------------------------------------
#imprimirPeces: lista de peces (pez) -> str
#Dada una lista de peces, imprime cada uno
#Ej:imprimirPeces(lista(pez('delicioso',3,10),None)) -> pez(tipo='delicioso', peso=3, puntaje=10)
#                                                       None
def imprimirPeces(listaDePeces):
    return printearLista(listaDePeces)
#Test:
#No aplica

#-----------------------------------------------------------------
# filtro: (X -> bool) lista(X)  -> lista(X)
# devuelve lista con los valores que operador da True
#Ej: *****************
def filtro(operador,L):
    if L==listaVacia:
        return listaVacia
    else:
        if operador(cabeza(L))==True:
            return lista(cabeza(L),filtro(operador,cola(L)))
        else:
            return filtro(operador,cola(L))
                
#Test:
valores= lista(6,lista(4,lista(8,listaVacia)))
assert filtro(lambda x: x<5,valores) == lista(4,listaVacia)
valores=lista('a',lista('b',lista('c',lista('d',listaVacia))))
assert filtro(lambda x: x >='b' and x<'d', valores)== lista('b', lista('c',listaVacia))

#----------------------------------------------------------------
# mapa:  (X -> Y) lista(X) -> lista(Y)
# devuelve lista con funcion aplicada a todos nodos
def mapa(f,L):
    if L==listaVacia:
        return listaVacia
    else: return lista(f(cabeza(L)),mapa(f,cola(L)))

#Test:
valores=lista(1,lista(2,lista(3,lista(4,listaVacia))))
assert mapa(lambda x: 10*x, valores) ==lista(10,lista(20,lista(30,lista(40,listaVacia))))
valores=lista('pedro',lista('juan',lista('diego',listaVacia)))
assert mapa(lambda x: x.upper(),valores)==lista('PEDRO',lista('JUAN',lista('DIEGO',listaVacia)))

#----------------------------------------------------------------
# fold: (X  X->X)  X lista(X) -> X
# procesa la lista con funcíon f y devuelve un valor
# el valor init se usa como valor inicial para
# procesar primer valor de la lista y como acumulador
#de resultados parciales
def fold(f,init,L):
    if L==listaVacia:
        return listaVacia
    elif cola(L)==listaVacia:
        return f(init,cabeza(L))
    else:
        return fold(f,f(init,cabeza(L)),cola(L))
#Test:
valores= lista(1,lista(2,lista(3, \
                            lista(4,listaVacia))))
assert fold(lambda x,y:x+y,0,valores)== 10
valores=lista('pedro',lista('juan',lista('diego',listaVacia)))
assert fold(lambda x,y:x+y,'',valores)=='pedrojuandiego'


#------------------------------------------------------------
#sumapuntaje: pez pez -> int
def sumaPuntaje(pez1,pez2):
    if pez1==None or pez1==0:
        return sumaPuntaje(pez('genérico',0,0),pez2)
    elif pez2==None or pez2==0:
        return sumaPuntaje(pez1,pez('genérico',0,0))
    elif type(pez1)==int:
        return sumaPuntaje(pez('generico0',0,pez1),pez2)
    else:
        return pez1.puntaje+pez2.puntaje
#Test
assert sumaPuntaje(None,None)==0
assert sumaPuntaje(pez('delicioso',4,15),None)==15
assert sumaPuntaje(pez('delicoso',4,15),pez('venenoso',3,-20))==-5
#--------------------------------------------------------------
#facil: pez -> pez (delicioso)
#Se le entrega un pez cualquiera
#Y lo transforma en delicioso
#Ej. facil(None) -> pez(tipo='delicioso', peso=5, puntaje=6)
#    facil(pez('venenoso',3,-30) -> pez(tipo='delicioso', peso=3, puntaje=30)
def facil(p):
    if p==None:
        return pez('delicioso',random.randint(1,5),random.randint(5,50))
    elif p.tipo=='delicioso':
        return p
    else:
        return pez('delicioso',p.peso,-(p.puntaje))
#Test:
assert (facil(pez('venenoso',3,-30)) == pez('delicioso',3,30))
assert facil(None).tipo=='delicioso'
assert facil(pez('delicioso',4,40))==pez('delicioso',4,40)
#---------------------------------------------------------------------
#normal pez -> pez=!None
#Recibe un pez, y lo retorna como el mismo si es
#delicioso o venenoso, y si es None retorna uno aleatorio
#EJ: normal(None)->pez(tipo='delicioso', peso=5, puntaje=6)
#    normal(pez('venenoso',3,-30)) -> (pez('venenoso',3,-30))
def normal(pez):
    if pez==None:
        return generarPez()
    else:
        return pez

#Test:
assert(normal((pez('venenoso',3,-30)) == (pez('venenoso',3,-30))))
assert (normal(pez('delicioso',4,25))== (pez('delicioso',4,25)))
assert(type(normal(None))==pez)
#-----------------------------------------------------------------
#esDelicioso: pez->bool
#retorna True si el pez ingresado es delicioso
#retorna False si el pez ingresado no es delicioso
#Ej:esDelicioso(None) -> False
#   esDelicioso(pez('delicioso',3,44))->True
def esDelicioso(pez):
    if pez==None:
        return False
    elif pez.tipo=='delicioso':
        return True
    else:
        return False
#Test:
assert esDelicioso(None)==False
assert esDelicioso(pez('delicioso',3,44))==True
assert esDelicioso(pez('venenoso',4,-7))==False
#-------------------------------------------------------------------
#esVenenoso: pez->bool
#Retorna True si el pez ingresado es venenoso, y false si no.
#Ej:esVenenoso(None) -> False
#   esVenenoso(pez('delicioso',3,44))->False
#   esVenenoso(pez('venenoso',4,-7)) -> True
def esVenenoso(pez):
    if pez==None:
        return False
    elif pez.tipo=='venenoso':
        return True
    else:
        return False
assert esVenenoso(None)==False
assert esVenenoso(pez('delicioso',3,44))==False
assert esVenenoso(pez('venenoso',4,-7))==True    
#---------------------------------------------------------------
#desarrollo str pez(x5) lista int int -> juego
#función complementaria a juego (ver más adelante)
#que recibe los mismos parámetros de esta más
#todos los parametros que se han definido durante la función
#por medio de la dificultad. Con su uso, se evita la repetición de código
#3 veces debido a la dificultad seleccionada. Considerese como parte de la
#función juego.
def desarrollo(continuar,p1,p2,p3,p4,p5,inventario,peso_hielo,dificultad):
            if continuar=='SI' or continuar=='si' or continuar=='sí' or continuar=='Sí':
                cuadrante=input('¿A qué cuadrante desea ir? (1,2,3,4,5)')
                if cuadrante=='1':
                    if p1==None:
                        print('Al parecer no hay nada...')
                        return juego(inventario,peso_hielo,dificultad)
                    else:
                        print('Se puede ver una forma moviéndose en el agua...')
                        pescar=input('¿Quieres pescar? ')
                        if pescar=='SI' or pescar=='si' or pescar=='sí' or pescar=='Sí':
                            print('¡Pescaste un ', p1.tipo,' ,peso ', p1.peso, ' ,puntaje ', p1.puntaje)
                            return juego(agregar(inventario,p1),(peso_hielo)-(p1.peso),dificultad)
                        else:
                            return juego(inventario,peso_hielo,dificultad)
                elif cuadrante=='2':
                    if p2==None:
                        print('Al parecer no hay nada...')
                        return juego(inventario,peso_hielo,dificultad)
                    else:
                        print('Se puede ver una forma moviéndose en el agua...')
                        pescar=input('¿Quieres pescar? ')
                        if pescar=='SI' or pescar=='si' or pescar=='sí' or pescar=='Sí':
                            print('¡Pescaste un ', p2.tipo,' ,peso ', p2.peso, ' ,puntaje ', p2.puntaje)
                            return juego(agregar(inventario,p2),(peso_hielo)-(p2.peso),dificultad)
                        else:
                            return juego(inventario,peso_hielo,dificultad)
                elif cuadrante=='3':
                    if p2==None:
                        print('Al parecer no hay nada...')
                        return juego(inventario,peso_hielo,dificultad)
                    else:
                        print('Se puede ver una forma moviéndose en el agua...')
                        pescar=input('¿Quieres pescar? ')
                        if pescar=='SI' or pescar=='si' or pescar=='sí' or pescar=='Sí':
                            print('¡Pescaste un ', p3.tipo,' ,peso ', p3.peso, ' ,puntaje ', p3.puntaje)
                            return juego(agregar(inventario,p3),(peso_hielo)-(p3.peso),dificultad)
                        else:
                            return juego(inventario,peso_hielo,dificultad)
                elif cuadrante=='4':
                    if p4==None:
                        print('Al parecer no hay nada...')
                        return juego(inventario,peso_hielo,dificultad)
                    else:
                        print('Se puede ver una forma moviéndose en el agua...')
                        pescar=input('¿Quieres pescar? ')
                        if pescar=='SI' or pescar=='si' or pescar=='sí' or pescar=='Sí':
                            print('¡Pescaste un ', p4.tipo,' ,peso ', p4.peso, ' ,puntaje ', p4.puntaje)
                            return juego(agregar(inventario,p4),(peso_hielo)-(p4.peso),dificultad)
                        else:
                             return juego(inventario,peso_hielo,dificultad)
                elif cuadrante=='5':
                    if p5==None:
                        print('Al parecer no hay nada...')
                        return juego(inventario,peso_hielo,dificultad)
                    else:
                        print('Se puede ver una forma moviéndose en el agua...')
                        pescar=input('¿Quieres pescar? ')
                        if pescar=='SI' or pescar=='si' or pescar=='sí' or pescar=='Sí':
                            print('¡Pescaste un ', p5.tipo,' ,peso ', p5.peso, ' ,puntaje ', p5.puntaje)
                            return juego(agregar(inventario,p5),(peso_hielo)-(p5.peso),dificultad)
                        else:
                            return juego(inventario,peso_hielo,dificultad)
                else:
                    print('Lo siento, no te he entendido')
                    return juego(inventario,peso_hielo,dificultad)
            elif continuar=='NO' or continuar=='no' or continuar=='No' or continuar=='nelpastel' or continuar=='nelson':
                print('peces atrapados:')
                imprimirPeces(inventario)
                delicioso=filtro(esDelicioso,inventario)
                venenoso=filtro(esVenenoso,inventario)
                print('Puntaje sumado por los peces venenosos: ', fold(sumaPuntaje,0,venenoso))
                print('Puntaje sumado por los peces deliciosos: ', fold(sumaPuntaje,0,delicioso))
                print('Puntaje final: ', fold(sumaPuntaje,0,inventario))
                nuevo=input('¿Quieres jugar de nuevo? ')
                if nuevo=='SI' or nuevo=='Sí'or nuevo=='sí' or nuevo=='si':
                    return start()
                else:
                    return print('gracias por jugar')
            else:
                print('Lo siento, no te he entendido')
                return juego(inventario,peso_hielo,dificultad)
                
#---------------------------------------------------------------
#juego lista int int(1,2,3) -> ---
#Función principal del juego 'La prueba del pingüino'
#donde se deberá pescar en 5 cuadrantes, ingresando los datos pedidos
#La idea es ganar la mayor cantidad de puntos, evitando que se rompa el hielo.
#Si pesco un pez delicioso, gano puntaje y sumo peso.
#Si pesco un pez venenoso, pierdo puntaje y sumo peso.
def juego(inventario,peso_hielo,dificultad):
    if peso_hielo <=0:
        print('¡Oh no! se ha roto el hielo porque llevabas mucho peso y has caído al agua!')
        print('peces atrapados:')
        imprimirPeces(inventario)
        delicioso=filtro(esDelicioso,inventario)
        venenoso=filtro(esVenenoso,inventario)
        print('Puntaje sumado por los peces venenosos: ', fold(sumaPuntaje,0,venenoso))
        print('Puntaje sumado por los peces deliciosos: ', fold(sumaPuntaje,0,delicioso))
        print('Puntaje final: ', fold(sumaPuntaje,0,inventario))
        nuevo=input('¿Quieres seguir jugando?')
        if nuevo=='SI' or nuevo=='Sí'or nuevo=='sí' or nuevo=='si':
            return start()
        else:
            return print('gracias por jugar')
    elif peso_hielo>0:
        peces=generarPeces(5)
        print('el peso que puedes soportar es ',peso_hielo)
        continuar=input('¿Quieres seguir pescando? ')
        if dificultad==1:
            peces=mapa(facil,peces)
            p1=sacarDeLista(peces,1)
            p2=sacarDeLista(peces,2)
            p3=sacarDeLista(peces,3)
            p4=sacarDeLista(peces,4)
            p5=sacarDeLista(peces,5)
            return desarrollo(continuar,p1,p2,p3,p4,p5,inventario,peso_hielo,dificultad)
        elif dificultad==2:
            peces=mapa(normal,peces)
            p1=sacarDeLista(peces,1)
            p2=sacarDeLista(peces,2)
            p3=sacarDeLista(peces,3)
            p4=sacarDeLista(peces,4)
            p5=sacarDeLista(peces,5)
            return desarrollo(continuar,p1,p2,p3,p4,p5,inventario,peso_hielo,dificultad)
        elif dificultad==3:
            p1=sacarDeLista(peces,1)
            p2=sacarDeLista(peces,2)
            p3=sacarDeLista(peces,3)
            p4=sacarDeLista(peces,4)
            p5=sacarDeLista(peces,5)
            return desarrollo(continuar,p1,p2,p3,p4,p5,inventario,peso_hielo,dificultad)

#----------------------------------------------------------------
#start:      -> juego
#Entrega las instrucciones iniciales del juego
#permite seleccionar dificultad y genera las condiciones
#iniciales, el peso del hielo y da una lista vacía como inventario.
def start():
    print('Bienvenid@ al juego de pesca!')
    print('Eres un pingüino muy hambriento, que')
    print('sale a buscar peces al rededor de')
    print('los 5 cuadrantes que conoce')
    print('¿En qué dificultad quieres jugar?')
    dificultad=input('(fácil, normal, difícil): ')
    peso_hielo=random.randint(10,30)
    if dificultad=='fácil' or dificultad=='facil' or dificultad=='Facil' or dificultad=='Fácil':
        return juego(listaVacia,peso_hielo,1)
    elif dificultad=='normal' or dificultad=='Normal':
        return juego(listaVacia,peso_hielo,2)
    elif dificultad=='difícil' or dificultad=='dificil' or dificultad=='Dificil' or dificultad=='Difícil':
        return juego(listaVacia,peso_hielo,3)
    else:
        print('Lo siento, no te he entendido')
        return start()
#------------------------------------------------------------------------
#Ejecución automática del programa
start()
