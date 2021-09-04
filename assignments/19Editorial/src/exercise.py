def main():
    # escribe tu código abajo de esta línea

    import math
    num_palabras = int(input("Dame el numero de palabras: "))
    num_paginas = math.ceil(num_palabras / 475)
    num_total = (num_paginas * 60)
    costo = 90 * num_total / 100
    print("El costo total es de:", costo)



if __name__ == '__main__':
    main()
