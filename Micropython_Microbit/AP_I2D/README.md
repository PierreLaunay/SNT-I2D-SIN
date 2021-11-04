# Activités Pratiques en I2D

3 Activités en micropython pour découvrir le micropython et la carte Microbit

- [Activité 0 - Initiation à Micropython sur MicroBit](Programmation_Microbit_MicroPython_AP_P0M.md)
- [Activité 1 – Led et délais](Programmation_Microbit_MicroPython_AP_P1M.md)
- [Activité 2 – structure de contrôle if else](Programmation_Microbit_MicroPython_AP_P2M.md)

Ces 3 activités permettent de découvrir :
- Le matériel ou hardware
  - l'afficheur de 25 LEDS (display)
  - le bouton poussoir A (button_a)
- Les bases de la programmation :
  - l'indentation en python et micropython
  - les conditions if, else et elif
  - les boucles while et for

Pour finir voici une **fonction** [clignotement](../software/microbit_clignotement.py) :

Cette fonction est créée avec le mot def, elle comporte 2 arguments TH et TB

Utilisation : clignotement(500,500) réalise un clignotement de la LED centrale toutes les secondes. T = TH + TB = 1000 ms = 1 s

Le programme complet fait clignoter la LED centrale en permanence au rythme de la seconde.

<pre>
<code>
# Add your MicroPython code here. E.g.
from microbit import *

def clignotement(TH,TB): # paramètres temps haut TH et temps bas TB en ms
    display.set_pixel(2,2,9) # on allume la led centrale
    sleep(TH)                # pendant le temps haut TH en ms
    display.set_pixel(2,2,0) # on éteint la led centrale
    sleep(TB)                # pendant le temps bas TB en ms

while True:                  # boucle sans fin
    clignotement(500,500)    # clignotement au rythme de la seconde
</code>
</pre>

Cette fonction clignotement pourra vous aider à faire la question 2c) de l'activité 1

Il faut évidemment modifier la boucle sans fin while True pour cette question.
