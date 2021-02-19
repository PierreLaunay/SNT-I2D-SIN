import microbit,utime
microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1) # init GPS NEO

while True : #boucle sans fin
    microbit.sleep(10)
    if microbit.uart.any() : # caractères reçus depuis le capteur de particules fines SDS011 ?
        content=microbit.uart.read() #lecture de 10 caractères voir DOC SDS011
        if 'GPRMC' in content :
            microbit.uart.init(baudrate=115200) # on remet la liaison série sur l'USB et on change la vitesse à 115200 bauds
            message = content.split()[0] #on prend le premier terme de GPRMC avant un caractère spécial
            print(message) # Pour voir les données brutes
            microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1)