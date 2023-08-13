#bisiesto(a) int->bool
#función que dado un año a
#retorna True si es un año bisiesto
#y false si no
#ejemplos: bisiesto(1900) -> False
#          bisiesto(2000) -> True
#          bisiesto(2016) -> True
def bisiesto(a):
    if a%4 == 0:
        if a%100 == 0:
            if a%400 == 0:
                return True
            elif a%100 ==  0:
                return False
        else:
            return True
    else:
        return False

#Test
assert(bisiesto(1900)==False)
assert(bisiesto(2000)==True)
assert(bisiesto(2016)==True)
            
        
    
    
