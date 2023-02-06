###Crear un arxiu de nom exercici1_A.py.
# En aquest arxiu s’hi crearà una funció on
# demanarà a l’usuari que inserti 2 números i
# el programa li dirà quin és el més gran i quin
# el més petit. Si son iguals sortirà que son iguals.
###

def numeros():
    x =int(input('introduce el valor 1:'))
    y =int (input('introduce el valor 2:'))

    if x > y:
        print("el valor {x} es mayor que {y}".format(x=x, y=y))
    elif x< y:
        print("el valor {x} es menor a {y}" .format(x=x, y=y))
    else:
        print("el valor {x} e {y} son iguales" .format(x=x, y=y))
numeros()