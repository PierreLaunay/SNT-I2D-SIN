import microbit,utime
microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1) # init de la liaison série du capteur de particules fines SDS011 , vitesse 9600 bauds
def verification(donnees): #on vérifie les données reçues voir doc SDS011
    checksum=sum(donnees[2:8])%256
    if (len(donnees) == 10) and (donnees[0] ==170) and (donnees[1] ==192) and (donnees[9] ==171) and (donnees[8] ==checksum) :
        return {"PM 2.5":(256*donnees[3]+donnees[2])/10, "PM 10":(256*donnees[5]+donnees[4])/10, "Temps":utime.ticks_ms()} #dictionnaires
    else:
        return {"PM 2.5":None, "PM 10":None,"Temps":utime.ticks_ms() }
while True : #boucle sans fin
    # microbit.sleep(10)
    if microbit.uart.any() : # caractères reçus depuis le capteur de particules fines SDS011 ?
        content=microbit.uart.read(10) #lecture de 10 caractères voir DOC SDS011
        message=[c for c in content] #pour transformer les 'bytes' en décimal
        microbit.uart.init(baudrate=115200) # on remet la liaison série sur l'USB et on change la vitesse à 115200 bauds
        #print(content) # Pour voir les données brutes
        #print(message) # Pour voir les données en décimal
        print(verification(message)) # Pour n'afficher que les PM 2.5 et PM 10
        microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1)  # init de la liaison série du capteur de particules fines SDS011