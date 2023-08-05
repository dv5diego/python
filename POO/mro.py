'''
Ejercicio basado en Method Resolution Order
'''
import mro

class A:
    def mostrarNombre(self):
        print("Clase A")

class B(A):
    def mostrarNombre(self):
        print("Clase B")

class E():
    def mostrarNombre(self):
        print("Clase E")

class C(E):
    def mostrarNombre(self):
        print("Clase C")

class D(A,C):
    def mostrarNombre(self):
        print("Clase D")


if __name__=="__main__":
    d=D()

    #Mostrar el orden de búsqueda de métodos de acuerdo a la jerarquía de clases, a partir de la clase D
    print(D.mro())