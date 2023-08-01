class Persona():
    def __init__(self,nombre):
        self.__nombre=nombre

    def mostrarDatos(self):
        print(f"Nombre: {self.__nombre}") 


class Empleado(Persona):
    def __init__(self,nombre,identificacion):
        super().__init__(nombre)
        self.__identificacion=identificacion

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Nro Identificacion: {self.__identificacion}") 

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self,value):
        self.__identificacion=value



if __name__=="__main__":
    empleado=Empleado("Diego","88306966")
    empleado.mostrarDatos()
