import math
import random

#distancia(x1,y1,x2,y2): num num num num num -> num
#Recibe dos puntos (x1,y1) y (x2,y2)
#y retorna la distancia (d)euclidiana entre
#ambos usando la fórmula math.sqrt((x1-x2)**2 + (y1-y2)**2)
#Ejemplos: distancia(0,0,0,2) -> 2
#          distancia(1,2,1,10) ->8
#          distancia(3,2,4,2) ->1
  
def distancia(x1,y1,x2,y2):
    d=math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d
#Test
assert(distancia(0,0,0,2) == 2)
assert(distancia(1,2,1,10) == 8)
assert(distancia(3,2,4,2) == 1)


#cerca(x1,y1,x2,y2,d): num num num num num -> bool
#Recibe dos puntos (x1,y1) y (x2,y2)
#y una disancia (d)y retorna un Booleano
#dependiendo si la distancia entre ambos es
#menor o igual a d (True) o mayor (False)
#Ejemplos: cerca(0,0,0,2,1) -> False
#          cerca(1,2,1,10,10) -> True
#          cerca(3,2,4,2,100) -> True
def cerca(x1,y1,x2,y2,d):
    if distancia(x1,y1,x2,y2)<=d:
        return True
    else:
        return False
#Test:
assert(cerca(0,0,0,2,1) == False)
assert(cerca(1,2,1,10,10) == True)
assert(cerca(3,2,4,2,100) == True)

#aleatorio(a,b) num num -> num
#Entrega un número real aleatorio
#en el intervalo [a,b], con a<b
#Ejemplos: aleatorio(1,100) -> 98
#          aleatorio(0,10) -> 9.8
#          aleatorio(20,30) -> 23.98124

def aleatorio(a,b):
    return random.uniform(a,b)

#Test
assert(1 <= aleatorio(1,100) and aleatorio(1,100) <= 100)
assert(1 <= aleatorio(1,10) and aleatorio(1,10) <= 10)
assert(20 <= aleatorio(20,30) and aleatorio(20,30) <=30)

#juego(x1,y1,x2,y2)-> int int num num (todos estos valores deben estar en el intervalo [-200,200]) -> str 
#La función analiza la distancia entre los puntos
#(x1,y1) y (x2,y2). Si esta es menor o igual a 4, el juego
#termina y da la opción de jugar de nuevo.
#Por el contrario, si esta es mayor a 4, se le indicará
#al jugador a qué distancia se encuentra (x1,y1) de (x2,y2)
#y este tendrá que ir dando instrucciones para trasladar el
#primer punto hacia el N, S, E u O una cantidad de metros
#entera hasta llegar a (x2,y2)
#Ejemplo: juego(0,0,4,0) -> juego(0,0,aleatorio(-200,200),aleatorio(-200,200)) o 'Gracias por jugar'
          
def juego(x1,y1,x2,y2):
    if cerca(x1,y1,x2,y2,4) == True:
        print('¡Felicidades, has encontrado el tesoro!')
        print('¿Quieres volver a jugar?')
        final = input('Responde SI o NO: ')
        if final == 'SI':
            return juego(0,0,aleatorio(-200,200),aleatorio(-200,200))
        elif final == 'NO':
            return print('Gracias por jugar')
        else:
            print('Lo siento, no te he entendido')
            return juego(x1,y1,x2,y2)
    elif cerca(x1,y1,x2,y2,4) == False:
        print('Estás a', distancia(x1,y1,x2,y2), 'metros del tesoro')
        cardinal = input('¿Hacia donde te quieres mover?: ')
        if cardinal == 'N':
            movimiento=int(input('¿Cuántos metros te quieres mover?: '))
            if movimiento+y1 > 200:
                print('¡Si te mueves tan lejos te saldrás de la laguna!')
                return juego(x1,y1,x2,y2)
            elif movimiento+y1 < 200:
                return juego(x1,movimiento+y1,x2,y2)
        elif cardinal == 'S':
            movimiento = int(input('¿Cuántos metros te quieres mover?: '))
            if y1-movimiento < -200:
                print('¡Si te mueves tan lejos te saldrás de la laguna!')
                return juego(x1,y1,x2,y2)
            elif y1-movimiento > -200:
                return juego(x1,y1-movimiento,x2,y2)
        elif cardinal == 'E':
            movimiento = int(input('¿Cuántos metros te quieres mover?: '))
            if movimiento+x1 > 200:
                print('¡Si te mueves tan lejos te saldrás de la laguna!')
                return juego(x1,y1,x2,y2)
            elif movimiento+x1 < 200:
                return juego(x1+movimiento,y1,x2,y2)
        elif cardinal == 'O':
            movimiento = int(input('¿Cuántos metros te quieres mover?: '))
            if x1-movimiento < -200:
                print('¡Si te mueves tan lejos te saldrás de la laguna!')
                return juego(x1,y1,x2,y2)
            elif x1-movimiento > -200:
                return juego(x1-movimiento,y1,x2,y2)
        else:
            print('¡Ese no es un cardinal válido!')
            return juego(x1,y1,x2,y2)

#INICIO DEL JUEGO
print('¡Bienvenido a La Prueba del delfín!')
print('Te has enterado que en un lago cercano, de forma cuadrada y dimensiones 400m')
print('hay un tesoro escondido, así que decides ir a buscarlo.')
print('')
print('')
print('Llegaste en tu bote al centro del lago, para comenzar a buscar,')
print('cuando se te pregunte, debes indicar en qué dirección te moverás.')
print('Debes elegir entre N (norte), S (sur), E(este) u O (oeeste).')
print('Además, cuando se te consulte "cuántos metros te quieres mover",')
print('deberás indicar un valor entero y positivo.')

juego(0,0,aleatorio(-200,200),aleatorio(-200,200))
        
        
            
            

