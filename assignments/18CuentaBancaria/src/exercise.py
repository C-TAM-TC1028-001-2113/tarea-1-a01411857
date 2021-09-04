def main():
    # escribe tu código abajo de esta línea
    saldo_anterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    num_cheques = int(input('Dame el numero de cheques: '))
    saldo = (saldo_anterior + ingresos - egresos - num_cheques * 13)
    saldo_final = saldo - (saldo * 0.075)
    print('El saldo final es', saldo_final)


if __name__ == '__main__':
    main()
