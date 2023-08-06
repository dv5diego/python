'''
Contar la cantidad de palabras dada una determinada frase.
'''

if __name__=="__main__":
    text="     esto es    un texto   si "

    text=text.lstrip().split(" ")
    phrase=[]
    
    for a in text:
        if(a!=""):
            phrase.append(a)

    print(f"La cantidad de palabras encontradas en la frase es: {len(phrase)}")
