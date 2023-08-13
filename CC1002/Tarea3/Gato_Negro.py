######### ----- Tarea 3 ----- #########
#ENTREGA FINAL#
## Importación de modulos ##
import estructura
import random

#lista de asignaturas
asignaturas=['Algebra','Biología','Cálculo','Computación','Ingeniería','Física']

## Creacion de estructuras mutables ##

# objeto: Nombre(str) Tipo(str) Cantidad(int) Felicidad(int)
#           Estudio(int) Materia(str)
estructura.mutable("objeto","Nombre Tipo Cantidad Felicidad Estudio Materia")

## Funciones Auxiliares ##
# IgualObjeto: objeto objeto -> bool
# Indica si dos objetos tienen los mismos
# parametros. Esta función será utilizada para
# hacer los test de la función leerInventario(Nombre)
# Ejemplo:  IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
#           objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")) -> True
def IgualObjeto(Obj1, Obj2):
    return ((Obj1.Nombre == Obj2.Nombre) and
            (Obj1.Tipo == Obj2.Tipo) and
            (Obj1.Cantidad == Obj2.Cantidad) and
            (Obj1.Felicidad == Obj2.Felicidad) and
            (Obj1.Estudio == Obj2.Estudio) and
            (Obj1.Materia == Obj2.Materia))
# Test
assert(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")))
assert not(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Fisica","Libro",1,-7,25,"Fisica")))
assert not(IgualObjeto(objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica"),
                    objeto("Codigo Secreto","Juego de Mesa",0,30,-7,"No aplica")))

#----------------------------------------------------------------------------------------       
# leerInventario: string -> lista
# Lee un archivo txt entregando una lista
# de objetos correspondientes a cada linea
# del archivo de texto.
# Condiciones: Para leer el archivo txt es
# necesario que este se encuentre en la misma
# carpeta que este archivo.py
# Recordar que 
# Ejemplo: 
def leerInventario(Nombre):
    inventario = [] # Lista vacia donde se guardarán los objetos
    inv = open(Nombre, 'r') # Se abre el archivo en modo lectura
    for linea in inv: # Se lee cada linea del archivo
        Obj = linea.split(";") # Separa cada string en una lista
        # tomando como separador ;
        # Luego crea el objeto tomando cada valor de la lista
        # anteriormente creada
        Obj = objeto(Obj[0], Obj[1], int(Obj[2]),
                     int(Obj[3]), int(Obj[4]), Obj[5][:-1])
        # Para el último valor (Obj[5]), el string termina con
        # un salto de linea \n , por lo que para ignorar
        # ese salto de linea se toman todos los caracteres
        # de ese último string menos el último
        inventario.append(Obj) # Se guarda el objeto en la lista
    return inventario
# Test
Inv = leerInventario("Inventario.txt")
Obj6 = objeto("Codigo Secreto","Juego de Mesa",1,30,-7,"No aplica")
Obj33 = objeto("Fisica","Libro",1,-7,25,"Fisica")
Obj19 = objeto("Essential Cell Biology","Libro",1,-7,20,"Biologia")
assert(IgualObjeto(Inv[6],Obj6))
assert(IgualObjeto(Inv[33],Obj33))
assert(IgualObjeto(Inv[19],Obj19))
#------------------------------------------------------------------------------------------------
#sacarDeInventario: lista, int -> lista
#recibe una lista de objetos y una cantidad de objetos a sacar de dicha lista, los
#objetos a sacar son escogidos de forma aleatoria y tienen que tener una
#cantidad disponible mayor a 0 para ser escogidos. Una vez escogido su
#cantidad disponible tiene que disminuir en 1 y guardar el objeto escogido en
#una lista de retornar.
#Ej: sacarDeInventario(leerInventario("Inventario.txt"),1)->[objeto(Nombre=Calculus,
#                                                        Tipo=Libro, Cantidad=0,
#                                                    Felicidad=-5, Estudio=25, Materia=Calculo)]
#sacarDeInventario(leerInventario("Inventario.txt"),2) -> [objeto(Nombre=King of New York,
#                                                         Tipo=Juego de Mesa, Cantidad=0, Felicidad=30, Estudio=-7,
#                                                          Materia=No aplica), objeto(Nombre=Apuntes CC1002, Tipo=Libro,
#                                                          Cantidad=0, Felicidad=-5, Estudio=30, Materia=Computacion)]
def sacarDeInventario(lista,cantidad):
    largo=[]
    nueva=[]
    for x in range(0,len(lista)-1):
        largo.append(x)
    while cantidad>0:
        R=random.sample(largo,1)
        for r in R:
            if lista[r].Cantidad!=0:
                lista[r].Cantidad=lista[r].Cantidad-1
                nueva.append(lista[r])
                cantidad-=1
    return nueva
#Test:
assert len(sacarDeInventario(leerInventario("Inventario.txt"),2))==2
a=sacarDeInventario(leerInventario("Inventario.txt"),8)
assert a[len(a)-1].Cantidad==0
assert a[0].Cantidad==0
#-------------------------------------------------------------------------------------------------
#guardarEnInventario: str -> None
#Recibe un objeto y aumenta la
#cantidad disponible de dicho objeto en 1.
#Ej: a=[objeto(Nombre=King of New York,
#Tipo=Juego de Mesa, Cantidad=0, Felicidad=30, Estudio=-7,
# Materia=No aplica), objeto(Nombre=Apuntes CC1002, Tipo=Libro,
#Cantidad=0, Felicidad=-5, Estudio=30, Materia=Computacion)]
#guardarEnInventario('King of New York',a) -> a[0].Cantidad==1
def guardarEnInventario(objeto,inventario):
    for x in inventario:
        if objeto==x.Nombre:
            x.Cantidad=x.Cantidad+1

#Test:
a=sacarDeInventario(leerInventario("Inventario.txt"),5)
guardarEnInventario(a[0].Nombre,a)
assert a[0].Cantidad==1
guardarEnInventario(a[2].Nombre,a)
assert a[2].Cantidad==1
guardarEnInventario(a[4].Nombre,a)
assert a[4].Cantidad==1

#--------------------------------------------------------------------------------------------------
#calcularFelicidad: lista -> num
#recibe una lista de objetos y la recorre sumando todos
#los índices de Felicidad entregando finalmente la suma total
#Ej:a=[objeto(Nombre=King of New York,
#Tipo=Juego de Mesa, Cantidad=0, Felicidad=30, Estudio=-7,
# Materia=No aplica), objeto(Nombre=Apuntes CC1002, Tipo=Libro,
#Cantidad=0, Felicidad=-5, Estudio=30, Materia=Computacion)]
#calcularFelicidad(a)->25
def calcularFelicidad(lista):
    i=0
    for x in lista:
        i=i+x.Felicidad
    return i
#Test:
a=[objeto('King of New York','Juego de Mesa',0,30,-7,'No aplica'), objeto('Apuntes CC1002','Libro',0,-5,30,'Computacion')]
b=[objeto('Monopoly','Juego de Mesa',0,200,-7,'No aplica'), objeto('Baldor','Libro',0,-40,30,'Algebra')]
c=[objeto('League of Legends board Game','Juego de Mesa',0,-500,-7,'No aplica'), objeto('Biografía de Camiroaga','Libro',0,999,30,'Otro')]
assert calcularFelicidad(a)==25
assert calcularFelicidad(b)==160
assert calcularFelicidad(c)==499
#-------------------------------------------------------------------------
#calcularEstudio: lista, str -> int
#recibe una lista de objetos y la recorre sumando
#todos los puntos de estudio y llevando una
#cuenta de cuantas veces se repite la materia
#entregada, para finalmente entregar la suma de todos los índices de Estudio
#más 10 veces la cuenta de la materia.
#Ej:a=[objeto('King of New York','Juego de Mesa',0,30,-7,'No aplica'), objeto('Apuntes CC1002','Libro',0,-5,30,'Computacion')]
#   calcularEstudio(a,'Computacion')->33
#   calcularEstudio(a,'Algebra')->23
def calcularEstudio(lista,materia):
    n=0
    indices=0
    for x in lista:
        if x.Materia==materia:
            n+=1
        indices=indices+x.Estudio
    return indices+(10*n)
#Test:
a=[objeto('King of New York','Juego de Mesa',0,30,-7,'No aplica'), objeto('Apuntes CC1002','Libro',0,-5,30,'Computacion')]
assert calcularEstudio(a,'Computacion')==33
assert calcularEstudio(a,'Algebra')==23
assert calcularEstudio(a,'Calculo')==23


#--------------------------------------------------------------------------
#Gato: int (1,2,3) -> bool
#se le entrega un nivel de dificultad 1, 2 o 3
# y dependiendo de él, retorna True si aparece un Gato
#o False si no lo Hace, de manera aleatoria, mientras más
#alto el nivel de dificultad, es menos probable que aparezca el gato
#Ej: Gato(1) -> True
#    Gato(2) -> True
#    Gato(3) -> False
def Gato(dificultad):
    if dificultad==1:
        r=random.randint(1,100)
        if r<50:
            return True
        else:
            return False
    if dificultad==2:
        r=random.randint(1,100)
        if r<40:
            return True
        else:
            return False

    if dificultad==3:
        r=random.randint(1,100)
        if r<30:
            return True
        else:
            return False

#Test:
a=Gato(1)
b=Gato(2)
c=Gato(3)
assert a==True or a==False
assert b==True or b==False
assert c==True or c==False
#-------------------------------------------------------------------------
#juego: lista, lista, int, int -> None
#Función principal del juego del Gato Negro, el funcionamiento
#Y las reglas del juego se describen de mejor forma en en cuerpo de
# la función start()
def juego(inventario,estudiante,dificultad,día=1):
    control=random.choice(asignaturas)
    print('Esta semana tienes control de',control,
          '¡Buena suerte en tu preparación!')
    felicidad=50
    estudio=50
    if dificultad==1:
        puntaje7=150
        díasEstudio=7
        print('El puntaje para el 7.0 es 150')
    elif dificultad==2:
        puntaje7=135
        díasEstudio=6
        print('El puntaje para el 7.0 es 135')
    elif dificultad==3:
        puntaje7=120
        díasEstudio=5
        print('El puntaje para el 7.0 es 120')
    registro={}
    while día<=díasEstudio:
        print('')
        print('')
        print('Día',día)
        print('Tu felicidad actual es:', felicidad)
        print('Tu estudio actual es:', estudio)
        print('')
        gato=Gato(dificultad)
        if gato==True:
            print('¡Ha aparecido el gato negro de la suerte!')
            print('')
            print('Procedes a acariciarlo y tu felicidad aumenta en 10')
            felicidad=felicidad+10
            print('')
        
        cantObjetos=random.randint(3,5)
        estante=sacarDeInventario(inventario,cantObjetos)
        print('Los libros que se ven en el estante de la biblioteca son:')
        indice=0
        for  i in estante:
            diccionario={'Nombre':i.Nombre,'Tipo':i.Tipo,'Cantidad':i.Cantidad,
                         'Felicidad':i.Felicidad,'Estudio':i.Estudio,'Materia':i.Materia}
            print(indice,':',diccionario['Nombre'],'Que corresponde a un',diccionario['Tipo'])
            print('Felicidad:',diccionario['Felicidad'],'Estudio:',diccionario['Estudio'],'Materia:',diccionario['Materia'])
            indice=indice+1
        agregar=int(input('¿Qué te gustaría pedir? (indica el índice del objeto): '))
        print('Se guarda en tu mochila',estante[agregar].Nombre)
        registro[estante[agregar].Nombre]=día
        for i in range(0,len(estante)-1):
            if i!=agregar:
                guardarEnInventario(estante[i].Nombre,inventario)
        estudiante.append(estante[agregar])
        felicidad=felicidad+estante[agregar].Felicidad
        estudio=estudio+estante[agregar].Estudio
        día=día+1
    print('')
    print('')
    print('Tu felicidad actual es: ', felicidad)
    print('Tu estudio actual es: ', estudio)
    print('')
    print('')
    print('¡Se terminó el tiempo para estudiar!')
    print('El registro de préstamos es el siguiente:')
    for x in registro:
        print(x,',fue pedido el día',registro[x])
    print('')
    print('Las notas finales son:')
    P1=max(min(7.0,(estudio*7.0)/puntaje7),1.0)
    print('P1=',P1)
    P2=max(min(7.0,(felicidad*7.0)/puntaje7),1.0)
    print('P2=',P2)
    Final=P1*0.6+P2*0.4
    print('Nota final=',Final)
    again=0
    while again==0:
        restart=input('¿Quieres jugar de nuevo? ')
        if restart=='SI' or restart=='Sí' or restart=='Si' or restart=='sí' or restart=='si':
            again=1
        elif restart=='NO' or restart=='No' or restart=='no':
            again=-1
        else:
            print('Lo siento, no te he entendido')
    if again==1:
        start()
    if again==-1:
        print('Gracias por jugar')
    


#-----------------------------------------------------------------------------------
#start: None -> juego
#Una vez invocada, se le presenta al
#jugador el juego del gato negro y el prestamo de la biblioteca y este introduce lo
#requerido para empezar el juego
def start():
    print('Bienvenido a: "El gato negro y el prestamo de Biblioteca"')
    print('')
    print('Los controles se acercan y debes prepararte, esta semana tienes')
    print('Un control muy importante que se te indicará más adelante')
    print('Cada día debes escoger en la biblioteca un prestamo para la semana')
    print('Ya sea un libro o un juego de mesa')
    print('Los juegos de mesas aumentan tu felicidad, pero disminuyen tu estudio')
    print('Los libros que hacen más sabio, pero menos feliz')
    print('¡Busca el equilibrio!')
    print('Además, si escoger un libro de la materia del control de la semana,')
    print('Ganarás 10 puntos extra, Lo mismo si aparece el gato negro')
    print('¡Buena suerte')
    print('Para empezar, debes decirme en qué dificultad quieres que sea tu semana,')
    print('en fácil, tienes 7 días para estudiar, en normal tienes 6, y en difícil')
    print('solamente estudiarás durante 5 días')
    dif=input('¿En qué dificultad quieres jugar? (fácil, normal o difícil) ')
    print('')
    print('')
    print('')
    if dif== 'fácil' or dif=='facil' or dif=='Facil' or dif=='Fácil' or dif=='1':
        return juego(leerInventario('Inventario.txt'),[],1)
    elif dif == 'normal' or dif=='Normal' or dif=='2':
        return juego(leerInventario('Inventario.txt'),[],2)
    elif dif == 'difícil' or dif=='dificil' or dif=='Difícil' or dif=='Dificil' or dif=='3':
        return juego(leerInventario('Inventario.txt'),[],3)
    else:
        print('Lo siento, no te he entendido')
        start()
#-------------------------------------------------------------------------------------
#Inicio:
start()


        
    
        
        
            
            
        
        
        
        
        
        
        
        
        

   
    



