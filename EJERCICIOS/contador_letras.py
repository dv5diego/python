'''
Instalar: pip install numpy
Contar la cantidad de letras dada una cadena de texto.
'''
import re


if __name__=="__main__":
    text="aasdsds44erer//668*8__lll52"

    result=re.findall("[a-zA-Z]", text)

    print(f"La cantidad de letras encontradas en la cadena de texto es: {len(result)}")