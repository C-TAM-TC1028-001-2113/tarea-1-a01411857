def main():
    # escribe tu código abajo de esta línea

    import math
    num_palabras = int(input("Dame el numero de palabras: "))
    numpaginas = math.ceil(num_palabras / 475)
    num_total = (numpaginas * 60)
    precio = 90 * num_total / 100
    print("El costo total es de:", precio)

if __name__ == '__main__':
    main()
