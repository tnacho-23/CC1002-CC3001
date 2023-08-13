#VERSIÓN A
#nombre de las estaciones de la linea 2 de norte a sur
linea2=['Vespucio Norte','Zapadores','Dorsal','Einstein',
        'Cementerios','Cerro Blanco','Patronato',
        'Puente Cal y Canto','Santa Ana','Los Héroes',
        'Toesca',"Parque O'Higgins",
        'Rondizzoni','Franklin','El Llano','San Miguel','Lo Vial',
        'Departamental','Ciudad del Niño','Lo Ovalle',
        'El Parrón','La Cisterna']
distancia = [0,3.1,2.5,2.8,3.0,2.7,3.2,10.0,10.1,10.2,10.3,10.4,
             10.5,10.6,10.7,10.8,10.9,11.0,11.1,11.2,11.3,11.4]

#-----------------------------------------------------------------
#indice: lista elemento(str) -> int
#recibe una lista y un elemento y retorna
#la posición del elemento en la lista
#si no está retorna -1
#Ej: indice(linea2,'Las Mercedes')->-1
#    indice(linea2,'La Cisterna')->21
#    indice(linea2,'Dorsal')->2
def indice(lista,elemento):
    for v in range(len(lista)):
        if lista[v]==elemento:
            return v
    return -1
#Test:
assert indice(linea2,'Las Mercedes')==-1
assert indice(linea2,'La Cisterna')==21
assert indice(linea2,'Dorsal')==2
#-----------------------------------------------------------------
#dista: str -> int
#se le entrega una estación,
#de la lista linea2, y entrega su
#distancia hasta el inicio de
#la linea, con el norte
#como inicio
#EJ: dista('Vespucio Norte')->0
#    dista('La Cisterna')-> 177.8
#    dista('Einstein')->8.4

def dista(estación):
    index=indice(linea2,estación)
    i=0
    for x in distancia:
        if indice(distancia,x)<=index:
            i=i+x
        else:
            i
            
    return i

#Test:
assert dista('Vespucio Norte')==0
assert dista('La Cisterna')==177.8
assert dista('Einstein')==8.399999999999999 #8.4

#----------------------------------------------------------------
#distTotal: str str -> num
#Recibe 2 estaciones de la lista linea2
#y entrega a qué distancia se encuentran una de
#la otra
#EJ: distTotal('Vespucio Norte','La Cisterna')->177.8
#    distTotal('La Cisterna','Vespucio Norte')->177.8
#    distTotal('Zapadores','Patronato') ->14.199999999999998
def distTotal(est1,est2):
    d1=dista(est1)
    d2=dista(est2)
    if d1>d2:
        return d1-d2
       
    else:
        return d2-d1
        

#Test:
assert distTotal('Vespucio Norte','La Cisterna')==177.8
assert distTotal('La Cisterna','Vespucio Norte')==177.8
assert distTotal('Zapadores','Patronato')==14.199999999999998 #14.2


#----------------------------------------------------------------
#-----------------------------------------------------------------
#VERSIÓN B
from estructura import *
#est: nombre(str) distancia(num)
crear('est','nombre distancia')

#nombre de las estaciones de la linea 2 de norte a sur
lineaDos=[est('Vespucio Norte',0),est('Zapadores',3.1),est('Dorsal',2.5),
        est('Einstein',2.8),est('Cementerios',3.0),est('Cerro Blanco',2.7),
        est('Patronato',3.2),est('Puente Cal y Canto',10.0),est('Santa Ana',10.1),
          est('Los Héroes',10.2),est('Toesca',10.3),est("Parque O'Higgins",10.4),
          est('Rondizzoni',10.5),est('Franklin',10.6),est('El Llano',10.7),
          est('San Miguel',10.8),est('Lo Vial',10.9),est('Departamental',11.0),
          est('Ciudad del Niño',11.1),est('Lo Ovalle',11.2),est('El Parrón',11.3),
          est('La Cisterna',11.4)]
#Test
assert len(linea2)==len(lineaDos)
#---------------------------------------------------------------------
#indiceB: lista elemento(str) -> int
#recibe una lista con estructuras
#donde uno de sus parámetros es nombre
#y retorna la posición de la estructura
#con ese nombre.
#Ej: indiceB(lineaDos,'Las Mercedes')->-1
#    indiceB(lineaDos,'La Cisterna')->21
#    indiceB(lineaDos,'Dorsal')->2
def indiceB(lista,elemento):
    for v in range(len(lista)):
        if lista[v].nombre==elemento:
            return v
    return -1

#Test:
assert indiceB(lineaDos,'Las Mercedes')==-1
assert indiceB(lineaDos,'La Cisterna')==21
assert indiceB(lineaDos,'Dorsal')==2

#------------------------------------------------------------------------
#distaB: str->int
#Recibe el nombre de una estación en la
#lista lineaDos, y retorna su distancia
#desde el origen (el punto más al norte)
#EJ: distaB('Vespucio Norte')->0
#    distaB('La Cisterna')-> 177.8
#    distaB('Einstein')->8.4
def distaB(estación):
    index=indiceB(lineaDos,estación)
    tot=0.0
    for x in lineaDos:
        if indiceB(lineaDos,x.nombre)<=index:
            tot=tot+x.distancia
        else:
            tot
    return tot

#Test
assert distaB('Vespucio Norte')==0
assert distaB('La Cisterna')==177.8
assert distaB('Einstein')==8.399999999999999 #8.4

#------------------------------------------------------------------------
#distTotalB: str str -> num
#recibe dos estaciones de la lista
#lineaDos y retorna la distancia entre ellas
#EJ: distTotalB('Vespucio Norte','La Cisterna')->177.8
#    distTotalB('La Cisterna','Vespucio Norte')->177.8
#    distTotalB('Zapadores','Patronato') ->14.199999999999998

def distTotalB(est1,est2):
    d1=dista(est1)
    d2=dista(est2)
    if d1>d2:
        return d1-d2
    else:
        return d2-d1
#Test:
assert distTotalB('Vespucio Norte','La Cisterna')==177.8
assert distTotalB('La Cisterna','Vespucio Norte')==177.8
assert distTotalB('Zapadores','Patronato')==14.199999999999998 #14.2

    

            
            
  
         
