#funció on demanarà a l’usuari que inserti 2 números i el programa li dirà quin és el més gran i quin el més petit.
# Si son iguals, no sortirà cap missatge.

def valores():
    valor = int(input('Inserta un valor: '))
    valor2 = int(input('Inserta otro valor: '))
    if (valor > valor2):
        print('el numero mayor es ' .format(valor=valor, valor2=valor2))
    if (valor < valor2):
        print('el numero menor es ' .format(valor=valor, valor2=valor2))
    else:
        pass
    return valor
valores()