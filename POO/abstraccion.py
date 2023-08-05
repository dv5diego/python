'''
Ejercicio donde se aplica la abstracción de métodos (uno de los pilares de la POO) 
en Python a través de la denominada interfaz formal, debido a que no existe la keyword interface como tal.
Los métodos que se definan clase Padre (Persona) no deben implementar, estos métodos deben implementarse 
de forma obligatoria en las clases que hereden (clases hijas).
'''
from abc import ABCMeta, abstractmethod

class Persona(metaclass=ABCMeta):

    @abstractmethod
    def caminar(self):
        pass
    
    @abstractmethod
    def correr(self):
        pass

class Estudiante(Persona):

    def caminar(self):
        print("Estoy caminando.")

    def correr(self):
        print("Estoy corriendo.")


if __name__=="__main__":
    estudiante=Estudiante()
    estudiante.caminar()
    estudiante.correr()