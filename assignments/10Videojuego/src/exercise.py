def main():
    # escribe tu código abajo de esta línea

    juegosnuevos = int(input("Dame la cantidad de juegos nuevos: "))
    juegos_usados = int(input("Dame la cantidad de juegos usados: "))
    total = (juegosnuevos * 1000) + (juegos_usados * 350)
    print("El total de tu compra es de:", total)


if __name__ == '__main__':
    main()
