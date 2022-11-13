from estructura import *
#estudiante: Nombre (str) Apellido(str) Rut(str) Curso(str)
#estructura que recibe cuarto atributos (nombe,apellido, rut, un curso
#en el que participa) en forma de str de un determinado estudiante
crear('estudiante', 'Nombre Apellido Rut Curso')
#Estructuras de ejemplo:
Esteban_Lopez=estudiante('Esteban', 'Lopez', '20499542-2','Filosofía')
Pablo_Jara=estudiante('Pablo', 'Jara', '20559829-4', 'Inglés')
#----------------------------------------------------------------------
#PerteneceACurso: estudiante str -> bool
#Recibe un estudiante y un curso y retorna True
#si el estudiante pertenece al curso y False si no.
#Ej.   Esteban_Lopez=estudiante('Esteban', 'Lopez', '20499542-2','Filosofía')
#      PerteneceACurso(Esteban_Lopez, 'Cálculo') -> False
#      Pablo_Jara=estudiante('Pablo', 'Jara', '20559829-4', 'Inglés')
#      PerteneceACurso(Pablo_Jara,'Inglés') -> True
def PerteneceACurso(estudiante, curso):
    if estudiante.Curso == curso:
        return True
    else:
        return False
#Tests
assert(PerteneceACurso(Pablo_Jara,'Inglés') == True)
assert(PerteneceACurso(Esteban_Lopez, 'Cálculo') == False)
assert(PerteneceACurso(Esteban_Lopez, 'Filosofía') == True)
#----------------------------------------------------------------------
#EsCompañero: estudiante estudiante -> bool
#Recibe dos estudiantes, si están en el mismo
#curso retorna True. De lo contrario entrega False.
#Ej. Esteban_Lopez=estudiante('Esteban', 'Lopez', '20499542-2','Filosofía')
#    Pablo_Jara=estudiante('Pablo', 'Jara', '20559829-4', 'Inglés')
#    EsCompañero(Esteban_Lopez,Pablo_Jara) -> False
def EsCompañero(Estudiante1, Estudiante2):
    if Estudiante1.Curso == Estudiante2.Curso:
        return True
    else:
        return False
#Test:
    assert(EsCompañero(Esteban_Lopez,Pablo_Jara) == False)

