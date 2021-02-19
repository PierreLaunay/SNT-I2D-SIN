# Emetteur radio serie
from microbit import *
import radio

radio.on() # mettre le module radio en marche
radio.config(channel=1)     # choisir un numéro de canal radio
radio.config(power=7)       # mettre le signal à puissance maximum
uart.init(115200)			# initialisation liaison série 115200 bauds

while True:                 # boucle infinie
	if uart.any():			# caractères reçus ? du clavier
		message=str(uart.read(),'UTF-8') # si oui, on lit le clavier
		radio.send(message) # on envoie le caractère reçu par radio