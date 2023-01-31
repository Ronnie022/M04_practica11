#función donde pide al usuario que inserte 2 números i el programa le dira cual és el mas mayor y cual es el mas menor
# Si son iguales no saldra ningun mensaje.

def valores():
    valor = int(input('Inserta un valor: '))
    valor2 = int(input('Inserta otro valor: '))
    if (valor > valor2):
        print('el numero mayor es {valor} y el menor es {valor2}'  .format(valor=valor, valor2=valor2))
    if (valor < valor2):
        print('el numero menor es {valor} y el mayor es {valor2}' .format(valor=valor, valor2=valor2))
    else:
        pass
valores()