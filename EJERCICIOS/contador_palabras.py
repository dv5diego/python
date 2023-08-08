'''
Contar la cantidad de palabras dada una determinada frase.
'''
import re

if __name__=="__main__":
    text="     esto es    un texto   // $ __._ --% %&**3.+\\ desde PYTHON"

    a=re.sub(r"[\W_]", " ", text)
    b=re.sub("[0-9]","",a)

    wordArrangement=[]

    for val in b.lstrip().split(" "):
        if(val!=""):
            wordArrangement.append(val)
    
    print(f"La cantidad de palabras encontradas en la frase es: {len(wordArrangement)}")
