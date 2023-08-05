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
    
    def __init__(self, nombre, nombre_padre, nombre_madre):
        Padre.__init__(self, nombre_padre)
        Madre.__init__(self, nombre_madre)
        self.__nombre=nombre

    def mostrarHijo(self):
        print(f"Hijo: {self.__nombre}")

    def mostrarPadre(self):
        Padre.mostrarPadre(self)

    def mostrarMadre(self):
        Madre.mostrarMadre(self)

class Computadora():
    def __init__(self):
        pass

class Nieto(Hijo):
    def __init__(self, nombre, nombre_padre, nombre_abuelo, nombre_abuela):
        Hijo.__init__(self, nombre_padre, nombre_abuelo, nombre_abuela)
        self.__nombre=nombre


if __name__ == '__main__':
    hijo=Hijo("CC","AA","BB")
    hijo.mostrarHijo()
    hijo.mostrarPadre()
    hijo.mostrarMadre()

    nieto=Nieto("DD","CC","AA","BB")

    '''
    1-Identificar si la variable hijo es una instancia de las clases Padre y Madre
    2-Identificar si la variable nieto es una instancia de las clases Padre, Madre, Hijo o Computadora
    '''
    is_instance1=isinstance(hijo, Padre)
    print(is_instance1)
    is_instance2=isinstance(hijo, Madre)
    print(is_instance2)

    is_instance3=isinstance(nieto, Padre)
    print(is_instance3)

    is_instance4=isinstance(nieto, Madre)
    print(is_instance4)

    is_instance5=isinstance(nieto, Hijo)
    print(is_instance5)

    is_instance6=isinstance(nieto, Computadora)
    print(is_instance6)

    print("*****"*10)

    '''
    1-Identificar si la clase Hijo es una subclase de las clases Padre y Madre
    2-Identificar si la clase Nieto es una subclase de las clases Padre, Madre e Hijo
    3-Identificar si las clases Hijo y Nieto son una subclase de la clase Computadora 
    '''
    is_subclass1=issubclass(Hijo, Padre)
    print(is_subclass1)
    is_subclass2=issubclass(Hijo, Madre)
    print(is_subclass2)

    is_subclass3=issubclass(Nieto, Hijo)
    print(is_subclass3)
    is_subclass4=issubclass(Nieto, Padre)
    print(is_subclass4)
    is_subclass5=issubclass(Nieto, Madre)
    print(is_subclass5)

    is_subclass6=issubclass(Hijo, Computadora)
    print(is_subclass6)
    is_subclass7=issubclass(Nieto, Computadora)
    print(is_subclass7)