#Una función donde pide al usuario que diga un número y le indicarà si és par o impar.
def numero():
    num = int(input('Indica un numero: '))
    if num%2==0:
        print("Es un numero par" .format(num=num))
    else:
        print("Es un numero impar" .format(num=num))


numero()