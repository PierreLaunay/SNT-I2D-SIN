# Python et Microbit Micropython

Nous allons depuis un programme en python piloté la carte Microbit et lui envoyer des commandes en micropython.

Nous pourrons récupérer la réponse et la traiter en python.

# Liaison série Python : Pyserial
Pour piloter la carte Microbit en python, nous allons travailler comme en REPL avec la liaison série.

La bibliothèque en python s'appelle [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html) pour l'installer sur un PC, on fera pip install pyserial

Mais le module dans le fichier s'appelle serial : import serial

Voici une [introduction](https://pyserial.readthedocs.io/en/latest/shortintro.html) pour l'utiliser

## Un exemple simple de lecture

<pre>
<code>
import serial # bibliothèque à installer pyserial : pip install pyserial

ser=serial.Serial('/dev/ttyACM0') #ouvre le port du microbit
ser.baudrate=115200
print(ser)
while True : #on lit en permanence la carte microbit
    if ser.in_waiting :
        texte=ser.read(ser.in_waiting).decode("utf-8")
        print(texte)
</code>
</pre>
