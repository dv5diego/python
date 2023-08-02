# DECORADORES
# *args   => recepciona N número de parámetros
# **kwargs=> parámetros con clave valor

def funcion_decoradora1(funcion_parametro):
    def funcion_interior(*args):
        print("Inicio de la funcion 1")
        funcion_parametro(*args)
        print("fin de la funcion 1")

    return funcion_interior

@funcion_decoradora1
def multiplicar(n1, n2):
    print("Desde funcion_decoradora1")
    print(f"resultado de la multiplicacion: {n1*n2}")


def funcion_decoradora2(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("Inicio de la funcion 2")
        funcion_parametro(*args, **kwargs)
        print("fin de la funcion 2")

    return funcion_interior

@funcion_decoradora2
def restar(n1, n2):
    print("Desde funcion_decoradora2")
    print(f"resultado de la resta: {n1-n2}")


if __name__=="__main__":
    multiplicar(4,8)
    print("***"*12)
    restar(n1=14, n2=8)