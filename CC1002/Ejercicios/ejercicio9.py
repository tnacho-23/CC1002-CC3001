#Campos:
#x:num
#y:num
#z:num
class vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    #EJ:a=vector(4,5,3)
    #b=vector(1,2,3)
    #c=vector(1,1,1)
    #d=vector(1,0,0)


    #toString: None -> str
    #devuelve un string con un vector
    #Ej: a.toString -> '(4,5,3)'
    def toString(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'


    #suma: vector->str
    #Suma el Vector a uno nuevo,
    #retornando el Vector
    #que represente la suma vectorial entre ambos.
    #Ej: a.suma(b)-> '(5,7,6)'
    def suma(self,V):
        nuevo=vector(self.x+V.x,self.y+V.y,self.z+V.z)
        return nuevo.toString()

    #mod: None -> num
    #retornará el módulo del
    #vector que llama al método.
    #Ej: a.mod()= 7.0710678118654755

    def mod(self):
        return pow(self.x**2+self.y**2+self.z**2,1/2)
#Test:
a=vector(4,5,3)
b=vector(1,2,3)
c=vector(1,1,1)
d=vector(1,0,0)
#Test de toString
assert a.toString()=='(4,5,3)'
assert d.toString()=='(1,0,0)'
#Test de suma
assert a.suma(b)=='(5,7,6)'
assert c.suma(d)=='(2,1,1)'
#Test de mod
assert d.mod()==1.0
assert b.mod()==3.7416573867739413
