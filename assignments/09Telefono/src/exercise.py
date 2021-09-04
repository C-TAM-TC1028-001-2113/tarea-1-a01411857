def main():
    # escribe tu código abajo de esta línea

    num_mensajes = float(input("Dame el numero de mensajes: "))
    num_megas = float(input("Dame el numero de megas: "))
    num_minutos = float(input("Dame el numero de minutos: "))
    costo_mensual = (num_mensajes + num_megas + num_minutos) * .8
    print("Tu costo mensual es de", costo_mensual)



if __name__ == '__main__':
    main()
