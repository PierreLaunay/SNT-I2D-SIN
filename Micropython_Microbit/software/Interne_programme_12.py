# Recepteur radio
from microbit import *
import radio

radio.on()
radio.config(channel=1)     # choisir un numéro de canal radio
radio.config(power=7)       # mettre le signal à puissance maximum

while True:                       
	message_recu = radio.receive()
	if message_recu is not None:  
		if message_recu == '\r' :   
			print(message)          
			message=''            
		else :                   
			message+=message_recu