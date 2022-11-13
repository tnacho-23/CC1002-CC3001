#octal: int>0 -> str
#función que recibe un número entero positivo
#en base 10 y retorna el mismo número,
#pero representado enoctal, como string.
#Ejemplos: octal(1234) -> '2322'
#          octal(77)   -> '115'
#          octal(8)    -> '10'


def octal(número):
    if número//8 == 0:
        return str(número%8)
    else:
        return str(octal(número//8))+str(número%8)

#Test
assert(octal(1234) == '2322')
assert(octal(77) == '115')
assert(octal(8) == '10')
assert(octal(4) == '4')


