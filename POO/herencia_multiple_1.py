class Padre:

    def __init__(self, nombre):
        self.__nombre=nombre

    def mostrarPadre(self):
        print(f"Nombre Padre: {self.__nombre}")

class Madre():

    def __init__(self, nombre):
        self.__nombre=nombre

    def mostrarMadre(self):
        print(f"Nombre Madre: {self.__nombre}")

class Hijo(Padre, Madre):
    
    def __init__(self, nombre, nombrePadre, nombreMadre):
        Padre.__init__(self, nombrePadre)
        Madre.__init__(self, nombreMadre)
        self.__nombre=nombre

    def mostrarHijo(self):
        print(f"Hijo: {self.__nombre}")

    def mostrarPadre(self):
        Padre.mostrarPadre(self)

    def mostrarMadre(self):
        Madre.mostrarMadre(self)


if __name__ == '__main__':
    hijo=Hijo("CC","AA","BB")
    hijo.mostrarHijo()
    hijo.mostrarPadre()
    hijo.mostrarMadre()