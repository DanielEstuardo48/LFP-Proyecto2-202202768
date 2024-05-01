from Errores import *
from Abstract  import Expression


class CrearDB(Expression):
    def __init__(self, nombre, fila, columna):
        self.funcion = 'CrearDB'
        self.nombre = nombre
        self.igual = None
        self.nueva = None
        self.funcion2 = 'CrearDB()'
        self.fila = fila
        self.columna = columna
        super().__init__(fila, columna)

    def ejecutarT(self):
        if self.nombre is not None:
            return 'use(' + self.nombre + ');'
        else:
            return 'Error: Falta el nombre de la base de datos'

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def operar(self, arbol):
        pass 

class EliminarDB(Expression):
    def __init__(self, nombre, fila, columna):
        self.funcion = 'EliminarDB'
        self.nombre = nombre
        self.igual = None
        self.nueva = None
        self.funcion2 = 'EliminarDB()'
        self.fila = fila
        self.columna = columna
        super().__init__(fila, columna)

    def ejecutarT(self):
        if self.nombre is not None:
            return 'db.dropDatabase()'
        else:
            return 'Error: Falta el nombre de la base de datos'

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def operar(self, arbol):
        pass

class CrearColeccion(Expression):
    def __init__(self, nombre, fila, columna):
        self.funcion = 'CrearColeccion'
        self.nombre = nombre
        self.igual = None
        self.nueva = None
        self.funcion2 = 'CrearColeccion("Calificacion")'
        super().__init__(fila, columna)

    def ejecutarT(self):
        if self.nombre is not None:
            return 'db.createCollection(' + self.nombre + ');'
        else:
            return 'Error: Falta el nombre de la colección de datos'

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def operar(self, arbol):
        pass



'''class Funcion(Expression):

#EliminarBD elimina = nueva EliminarBD();
    def __init__(self, funcion, nombre, igual, nueva, funcion2, fila, columna):
        self.funcion = funcion
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.funcion2 = funcion2
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        if self.funcion == 'CrearDB':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.funcion2 == 'CrearDB()':
                            return 'use(' + self.nombre + ');'
                        else:
                            return 'Error: Falta la palabra reservada CrearDB()'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
        elif self.funcion == 'EliminarDB':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.funcion2 == 'EliminarDB()':
                            return 'db.dropDatabase()'
                        else:
                            return 'Error: falta la palabra reservada EliminarDB()'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
        elif self.funcion == 'CrearColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.funcion2 == 'CrearColeccion("Calificacion")':
                            return 'db.createCollection(' + self.nombre + ');'
                        else:
                            return 'Error: Falta la palabra reservada CrearColeccion(“NombreColeccion”)'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la coleccion de datos'
        else:
            return Errores(self.funcion,"Sintactico", self.getFila(), self.getColumna())       

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()'''