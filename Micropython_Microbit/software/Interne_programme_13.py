# Recepteur radio
from microbit import *
import radio

radio.on()
radio.config(channel=1)     # choisir un numéro de canal radio
radio.config(power=7)       # mettre le signal à puissance maximum
message = ''
while True:
    message_recu = radio.receive()
    if message_recu is not None:
        if message_recu == '\r' :
            print(message)
            message = ''
        else :
            message = message + message_recu
    if uart.any():			# caractères reçus ?
        message_serie = str(uart.read(), 'UTF-8')
        radio.send(message_serie)