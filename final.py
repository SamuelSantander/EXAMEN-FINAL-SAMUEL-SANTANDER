import random

# LISTA 
lista = [random.randint(1, 100) for i in range(10)]

print("LISTA ORIGINAL:")
print(lista)


# BURBUJA 
def burbuja(lista):
    numeros = lista.copy()  # Copiamos la lista para conservar la original
    iteraciones = 0

    # Comparamos numeros vecinos. Si no hay cambios en una vuelta,
    # significa que la lista ya esta ordenada y podemos terminar.
    for i in range(len(numeros) - 1):
        hubo_intercambio = False

        for j in range(len(numeros) - 1 - i):
            iteraciones += 1

            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    return numeros, iteraciones


#SELECTION SORT
def seleccion(lista):
    numeros = lista.copy()
    iteraciones = 0

    # Buscamos el numero mas pequeno de la parte no ordenada
    for i in range(len(numeros) - 1):
        posicion_menor = i

        for j in range(i + 1, len(numeros)):
            iteraciones += 1

            if numeros[j] < numeros[posicion_menor]:
                posicion_menor = j

        # Colocamos el menor numero en su posicion correcta
        numeros[i], numeros[posicion_menor] = numeros[posicion_menor], numeros[i]

    return numeros, iteraciones


# MENU
print("\nMENU DE ORDENAMIENTO")
print("1. Bubble Sort (metodo burbuja)")
print("2. Selection Sort (metodo seleccion)")

opcion1 = input("Elige el primer metodo (1 o 2): ")
opcion2 = input("Elige el segundo metodo (1 o 2): ")

if opcion1 not in ["1", "2"] or opcion2 not in ["1", "2"]:
    print("Error: debes elegir 1 o 2.")
elif opcion1 == opcion2:
    print("Error: debes elegir dos metodos diferentes.")
else:
    # primer metodo elegido
    if opcion1 == "1":
        resultado1, vueltas1 = burbuja(lista)
        nombre1 = "Bubble Sort"
    else:
        resultado1, vueltas1 = seleccion(lista)
        nombre1 = "Selection Sort"

    # }segundo metodo elegido
    if opcion2 == "1":
        resultado2, vueltas2 = burbuja(lista)
        nombre2 = "Bubble Sort"
    else:
        resultado2, vueltas2 = seleccion(lista)
        nombre2 = "Selection Sort"

    # RESULTADOS
    print("\nRESULTADOS")
    print("Lista original:", lista)
    print(nombre1, "ordena la lista asi:", resultado1)
    print("Iteraciones de", nombre1 + ":", vueltas1)

    print(nombre2, "ordena la lista asi:", resultado2)
    print("Iteraciones de", nombre2 + ":", vueltas2)

    #COMPARAR
    print("\nCOMPARACION")

    if vueltas1 < vueltas2:
        print(nombre1, "utilizo menos iteraciones.")
    elif vueltas2 < vueltas1:
        print(nombre2, "utilizo menos iteraciones.")
    else:
        print("Los dos metodos utilizaron la misma cantidad de iteraciones.")

    print("\nEn este programa, una iteracion es una comparacion entre dos numeros.")
