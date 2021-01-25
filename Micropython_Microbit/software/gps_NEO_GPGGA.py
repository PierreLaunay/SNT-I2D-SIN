import microbit,utime
microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1) # init GPS NEO

while True : #boucle sans fin
    microbit.sleep(10)
    if microbit.uart.any() : # caractères reçus depuis le capteur GPS  ?
        content=microbit.uart.read() #lecture de la trame du GPS NEO
        microbit.uart.init(baudrate=115200) # on remet la liaison série sur l'USB et on change la vitesse à 115200 bauds
        for message in  content.split() :
            if 'GPGGA' in message:
                print(message)
        microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1)