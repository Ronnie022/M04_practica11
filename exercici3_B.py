#Una función donde le pide al usuario la edad y los ingresos que tiene mensuales.
#Si la respuesta de l’edat és igual o mayor de 18 años y los ingresos mayores de 1200,
#El mensaje serà “És necessario que hagas la declaració de hacienda”.
#En el caso que alguna de las dos opciones no cumpla, el mensaje sera “Todavia no puedes hacer la declaración”.
def usuario():
    edad = int(input('Que edad tienes?: '))
    ingresos = int(input('Que ingresos tienes mensuales?:'))
    if edad>=18  and ingresos>1200:
        print("Es necesario que hagas la declaracion de hacienda" .format(edad=edad, ingresos=ingresos))
    else:
        print('Todavia no puedes hacer la declaracion' .format(edad=edad, ingresos=ingresos))

usuario()