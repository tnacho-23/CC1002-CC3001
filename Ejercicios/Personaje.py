from Arma import *
#Campos:
#ataque: int
#vida: int
#defensa: int
class Personaje:
    #constructor
    def __init__(self,ataque,vida,defensa):
        self.ataque=ataque
        self.vida=vida
        self.defensa=defensa
        self.armas=[]
    #Ej:link=Personaje(40,50,30)
    #   steve=Personaje(60,80,5)
    #   kirby=Personaje(10,180,10)
    #    link.vida->50
    #atacar: Personaje -> Personaje
    #Dado otro personaje, reduce su vida en una cantidad igual a la
    #diferencia entre ataque del personaje y defensa del enemigo
    #solo si el ataque del atacante es mayor que la defensa del enemigo.
    #Si el enemigo queda con vida negativa, se deja en 0
    #Ej: steve.atacar(link) implica que: link.vida==10
    #    kirby.atacar(link) implica que: link.vida==50
    def atacar(self,enemigo):
        if self.ataque>enemigo.defensa:
            enemigo.vida=enemigo.vida-(self.ataque-enemigo.defensa)
            if enemigo.vida<=0:
                enemigo.vida=0

    #isAlive: None -> bool
    #retorna True si la vida del personaje es positiva y False si no
    #Ej: link.isAlive() -> True
    #    Personaje(10,0,10).isAlive -> False
    def isAlive(self):
        return self.vida>0

    #heal: int -> None
    #Aumenta la vida del personaje en la cantidad señalada
    #Ej: link.heal(10) implica que: link.vida==60
    def heal(self,cantidad):
        self.vida=self.vida+cantidad

    #equipar: Arma -> None
    #Aumenta el ataque del personaje en una cantidad igual al daño
    #del Arma, además, añade el Arma a la lista armas que tiene el personaje.
    #Ej:steve.equipar(escalibur) implica que: steve.ataque==70
    def equipar(self,Arma):
        self.armas.append(Arma)
        self.ataque=self.ataque+Arma.daño

#Test:
link=Personaje(40,50,30)
steve=Personaje(60,80,5)
kirby=Personaje(10,180,10)
excalibur=Arma(10)
assert excalibur.daño==10
assert steve.ataque==60
steve.equipar(excalibur)
assert steve.ataque==70
assert link.vida==50
steve.atacar(link)
assert link.vida==10
assert link.isAlive()==True
steve.atacar(link)
assert link.vida==0
assert link.isAlive()==False
link.heal(60)
assert link.vida==60
kirby.atacar(link)
assert link.vida==60
    
   
    
        
        
