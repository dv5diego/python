if __name__ == '__main__':
    set_countries={"pe","nz","ge","ir"}

    size=len(set_countries)

    print(f"Tamaño del conjunto: {size}")

    #Verificar si un determinado valor existe en el conjunto
    print("pe" in set_countries)
    print("fr" in set_countries)

    #Agregar valores a un conjunto
    set_countries.add("pe")
    set_countries.add("pa")

    print(f"Datos agregados al conjunto: {set_countries}")

    #Actualizar valores de un conjunto
    set_countries.update({"ar","br"})
    print(f"Datos actualizados del conjunto: {set_countries}")

    #Remover valores de un conjunto
    set_countries.remove("br")
    #Al no encontrar el registro, remove lanza un error
    # set_countries.remove("bo")
    print(f"Valores removidos: {set_countries}")

    #Aplicar discard en un conjunto
    set_countries.discard("ar")
    #Al no encontrar el registro, "remove" no lanza un error, permite continuar con la ejecución
    set_countries.discard("bo")
    print(f"Datos del conjunto, al aplicarse discard: {set_countries}")

    #LIMPIAR EL CONJUNTO
    set_countries.clear()
    print(f"Limpiar el conjunto: {set_countries}")

