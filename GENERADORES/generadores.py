# Generadores: almacenan el valor de acuerdo a como se requiera, no se arma toda la lista para luego
# mostrarla. Ahorro de recursos, no consume mucha memoria.

def generarPares(limite):
    i=1
    while i<limite:
        yield i*2
        i=i+1

if __name__=="__main__":

    numeros_pares=generarPares(10)
    print(next(numeros_pares))
    print(next(numeros_pares))
    print(next(numeros_pares))