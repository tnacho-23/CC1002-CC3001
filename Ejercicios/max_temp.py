from lista import *
#maxTemp: lista -> float
#Recibe una lista de temperaturas de un paciente
#y retorna cuál es el valor más alto de la lista.
#Si la lista está vacía, retorna 0.
#Ej: temp_de_Juan=lista(38,lista(38,lista(39,lista(37,lista(40,lista(37,lista(29,None)))))))
#    maxTemp(temp_de_Juan) -> 40
#temp_mono_de_nieve=lista(-2,lista(-4,lista(4,lista(-7,None))))
#maxTemp(temp_mono_de_nieve) -> 4
def maxTemp(lista):
    if lista==listaVacia:
        return 0
    else:
        return max(cabeza(lista),maxTemp(cola(lista)))

#Test
temp_mono_de_nieve=lista(-2,lista(-4,lista(4,lista(-7,None))))
temp_de_Juan=lista(38,lista(38,lista(39,lista(37,lista(40,lista(37,lista(29,None)))))))
assert maxTemp(temp_de_Juan)== 40
assert maxTemp(temp_mono_de_nieve) == 4
assert maxTemp(listaVacia) == 0
