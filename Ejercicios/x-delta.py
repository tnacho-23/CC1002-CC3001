#serieRec: float float -> float
#recibe dos parámetros (x, delta) y
#calcula la serie 1/x+1/(x+1)+1/(x+2) …
#hasta que el termino 1/(x+m) sea menor que delta
#Ejemplos: serieRec(2,10) -> 0
#          serieRec(1,0.1) -> 2.9289682539682538
#          serieRec(1,0.001) -> 7.485470860550341

def serieRec(x,delta):
    if (1/x)<delta:
        return 0
    else:
        return (1/x)+serieRec(x+1,delta)

#Test
assert(serieRec(2,10) == 0)
assert(serieRec(1,0.1) == 2.9289682539682538)
assert(serieRec(1,0.001) == 7.485470860550341)

#----------------------------------------------------
#serie: float -> float
#Retorna elresultado de la serie 1/1+1/2+ … + 1/n hasta q
#que 1/n sea menor que un parámetro delta
#Ejemplos: serie(0.2) -> 2.283333333333333
#          serie(0.1) -> 2.9289682539682538
#          serie(0.001) -> 7.485470860550341

def serie(delta):
    return serieRec(1,delta)
#Test: 
assert(serie(0.2) == 2.283333333333333)
assert(serie(0.1) == 2.9289682539682538)
assert(serie(0.001) == 7.485470860550341)


