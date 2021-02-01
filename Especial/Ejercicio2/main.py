from Autobus import *
eleccion=random.choice(tipos)
if eleccion == 'coche':
        coche = Autobus(200, 15000, 5)
        tarifa= coche.capacidad * 100
        print('Soy un auto', tarifa)
        print ('Mi tarifa total es de:', coche.capacidad)

elif eleccion == 'autobus':
        autobus = Autobus(250, 30000, 40)
        tarifa = autobus.capacidad * 100
        print('Soy un autobus',tarifa)
        print ('Mi tarifa total es de:', autobus.capacidad)

else:
        trailer = Autobus(300, 300000, 6 )
        tarifa = trailer.capacidad * 100
        print('Soy un trailer',tarifa)
        print('mi tarifa total es de:', trailer.capacidad)



