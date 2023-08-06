'''
Contar la cantidad de números dada una cadena de texto.
'''
import re

if __name__=="__main__":
    text="aasdsds44erer//668*8"

    result=re.findall("[0-9]", text)

    print(f"La cantidad de números encontradas en la cadena de texto es: {len(result)}")