'''
Identificar si entre las cadenas dadas se presenta o no la distancia de Hamming.
'''

if __name__=="__main__":
    text1="Sudamerica"
    # Descomentar para comparar cadenas y presentar un valor de 0
    # text1="Suramerica"
    text2="Suramerica"

    distance=0

    if(len(text1)!=len(text2)):
        raise("Los textos tienen un tamaño diferente.")

    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            distance=+1

    print(f"La distancia es de: {distance}")
