#notafinal(n): float -> string
#entregar la calificación
#del exámen de grado en función
# de la nota obtenida
#Ejemplos: notafinal(4.0)-> 'aprobado'
#          notafinal(6.3)-> 'aprobado con distinción máxima'
#          nota final(3.9)->'reprobado'
def notafinal(n):
    if n>=1 and n<4:
        return 'reprobado'
    elif n>=4 and n<5:
        return 'aprobado'
    elif n>=5 and n<6:
        return 'aprobado con distinción'
    elif n>=6 and n<=7:
        return 'aprobado con distinción máxima'
    else:
        return 'fuera de rango'

#Test
assert(notafinal(4.0)== 'aprobado')
assert(notafinal(6.3)=='aprobado con distinción máxima')
assert(notafinal(3.9)=='reprobado')

    
