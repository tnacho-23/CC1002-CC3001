#suma int int -> int
#recibe dos números enteros, x e y,
#x<=y, y calcula la suma de todos los enteros
#entre x e y, con ambos incluidos
#Ejemplos: suma(1,3) -> 6
#          suma(0,4) -> 10
#          suma(2,20) -> 209

def suma(x,y):
    if x==y:
        return x
    elif x<y:
        return x + suma(x+1,y)
#Test
assert(suma(1,3) == 6)
assert(suma(0,4) == 10)
assert(suma(2,20) == 209)
    


    
