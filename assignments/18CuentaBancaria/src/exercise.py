def main():
    # escribe tu código abajo de esta línea

    saldoanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame el valor de los ingresos: "))
    egresos = float(input("Dame el valor de los egresos: "))
    num_cheques = float(input("Dame el numero de cheques: "))
    saldo = (saldoanterior + ingresos - egresos - num_cheques * 13)
    saldo_final = saldo - (saldo * 0.075)
    print("El saldo final es", saldo_final)


if __name__ == '__main__':
    main()
