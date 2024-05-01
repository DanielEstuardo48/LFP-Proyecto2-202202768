from Funciones import *
from Errores import *
from Lexema import *

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores

n_linea = 1
n_columna = 1
instrucciones = []
lista_lexemas = []
lista_errores = []


def intruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0


    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char.isupper() or char.islower():       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0

        elif char == '=':
            #! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna)

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char =="\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(Errores(char,"Lexico", n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1


    return lista_lexemas

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == ' ' or char == ';':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None



def operar():
    global lista_lexemas
    instrucciones = []

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.lexema == 'CrearBD':  # Verificar si el lexema representa la creación de una base de datos
            nombre_lexema = lista_lexemas.pop(0)  # Obtener el nombre de la base de datos
            nombre = nombre_lexema.lexema if nombre_lexema else None
            instruccion = CrearDB(nombre, lexema.getFila(), lexema.getColumna())
            instrucciones.append(instruccion)
        elif lexema.lexema == 'EliminarBD':  # Verificar si el lexema representa la eliminación de una base de datos
            nombre_lexema = lista_lexemas.pop(0)  # Obtener el nombre de la base de datos
            nombre = nombre_lexema.lexema if nombre_lexema else None
            instruccion = EliminarDB(nombre, lexema.getFila(), lexema.getColumna())
            instrucciones.append(instruccion)
        elif lexema.lexema == 'CrearColeccion':  # Verificar si el lexema representa la creación de una colección
            nombre_lexema = lista_lexemas.pop(0)  # Obtener el nombre de la colección
            nombre = nombre_lexema.lexema if nombre_lexema else None
            instruccion = CrearColeccion(nombre, lexema.getFila(), lexema.getColumna())
            instrucciones.append(instruccion)

    return instrucciones





def operar_():
    return operar()

def getErrores():
    global lista_errores
    return lista_errores



resultado_instrucciones = operar_()

for respuesta in resultado_instrucciones:
    print(respuesta.ejecutarT())




'''for respuesta in resultado_instrucciones:
    print(respuesta.ejecutarT(None))'''