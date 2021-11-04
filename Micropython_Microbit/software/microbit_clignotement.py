# Add your MicroPython code here. E.g.
from microbit import *

def clignotement(TH,TB): # paramètres temps haut TH et temps bas TB en ms
    display.set_pixel(2,2,9) # on allume la led centrale
    sleep(TH)                # pendant le temps haut TH en ms
    display.set_pixel(2,2,0) # on éteint la led centrale
    sleep(TB)                # pendant le temps bas TB en ms

while True :                # boucle sans fin
    clignotement(500,500)   # clignotement au rythme de la seconde
