'''
Mostrar en un arreglo sola las letras a partir de una cadena de texto dada.
'''
import re


if __name__=="__main__":
    text="aasdsds44erer//668*8"

    result=re.findall("[a-zA-Z]", text)

    print(result)