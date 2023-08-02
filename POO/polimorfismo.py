class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Voy caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Voy en bicicleta')


def main():
    persona = Persona('Diego')
    persona.avanza()

    ciclista = Ciclista('Dev')
    ciclista.avanza()


if __name__ == '__main__':
    main()