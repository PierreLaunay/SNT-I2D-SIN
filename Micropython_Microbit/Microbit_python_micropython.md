# Python et Microbit Micropython

Nous allons depuis un programme en python piloté la carte Microbit et lui envoyer des commandes en micropython.

Nous pourrons récupérer la réponse et la traiter en python.

# Liaison série Python : Pyserial
Pour piloter la carte Microbit en python, nous allons travailler comme en REPL avec la liaison série.

La bibliothèque en python s'appelle [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html) pour l'installer sur un PC, on fera pip install pyserial

Mais le module dans le fichier s'appelle serial : import serial

Voici une [introduction](https://pyserial.readthedocs.io/en/latest/shortintro.html) pour l'utiliser

Pour faire simple nous avons 3 parties :
- Une partie pour initialiser le port
- Une partie pour lire  avec ser.in_waiting caractère(s) reçu(s)? ser.read pour les lire
- Une partie pour écrire des commandes
## Un exemple simple de lecture

<pre>
<code>
import serial # bibliothèque à installer pyserial : pip install pyserial

ser=serial.Serial('/dev/ttyACM0') #ouvre le port du microbit
ser.baudrate=115200 # vitesse 115200 bauds par défaut
print(ser)  #on vérifie que le port est bien ouvert ainsi que ses attributs
while True : #on lit en permanence la carte microbit
    if ser.in_waiting : # caractères reçus ?
        texte=ser.read(ser.in_waiting).decode("utf-8") #on lit les caractères et on les convertit en utf-8
        print(texte) #afficher le texte reçu
</code>
</pre>

À partir de cet exemple, on peut faire beaucoup de variantes.

Exemple : sauvegarder le texte dans un fichier.

## Exemple avec des commandes

<pre>
<code>
from collections import Counter
import re,serial,time # bibliothèque à installer pyserial : pip install pyserial
ser=serial.Serial('/dev/ttyACM0') #ouvre le port du microbit
ser.baudrate=115200 # le baudrate est à 115200 bauds par défaut
print(ser) #on affiche les infos du port série
# Appuyer sur le bouton reset de la carte Microbit avant de lancer
messages=[b'import microbit\r\n',b'info_pin = {i:dir(eval("microbit."+i)) for i in dir(microbit) if i.startswith("pin")}\r\n',b'info_pin\r\n']
for message in messages: ser.write(message) # on import la bibliothèque microbit, on récupère la liste des broches et leurs méthodes puis on l'affiche
debut=time.time() #on initilaise le temps
texte="" #on prendre un texte vide pour commencer
while time.time()-debut < 1: #on récupère pendant 1 s les caractères reçus
    if ser.in_waiting : #caractère reçu ?
        texte+=ser.read(ser.in_waiting).decode("utf-8")#on le lit et on le transforme en utf8
print(texte) # on affiche le texte reçu
info_pin=eval(re.findall(r"({.*?})",texte,re.S)[-1]) # on ne garde que le dictionnaire
ser.close() #on ferme la liaison série
# fin de la récupération des données avec Microbit, la partie en dessous ne peut être faite sur microbit Counter n'existe pas dans collections
infos = {tuple([k for k,v in info_pin.items() if tuple(v) ==i]):set(i)
         for i in Counter([tuple(l) for l in info_pin.values()]).keys()} #on retrouve le noms des broches qui ont les mêmes méthodes
print(infos) #on affiche le nouveau dictionnaire
commun = list(infos.values())[0].intersection(*list(infos.values()))
infoscom_pins = {'methodes communes': sorted(commun)}
infoscom_pins.update({i:set(j) - commun for i, j in infos.items()})
print("Résultat :",infoscom_pins)
for i,j in infoscom_pins.items() :
    if type(i) is tuple : print(len(i),i,j)
    else : print(i,j)
</code>
</pre>

Voici la réponse finale :
<pre>
<code>
methodes communes ['NO_PULL', 'PULL_DOWN', 'PULL_UP', 'get_mode', 'get_pull', 'read_digital', 'set_analog_period', 'set_analog_period_microseconds', 'set_pull', 'write_analog', 'write_digital']
3 ('pin3', 'pin4', 'pin10') {'read_analog'}
3 ('pin2', 'pin0', 'pin1') {'read_analog', 'is_touched'}
13 ('pin7', 'pin6', 'pin5', 'pin20', 'pin8', 'pin9', 'pin13', 'pin12', 'pin11', 'pin16', 'pin15', 'pin14', 'pin19') {'get_analog_period_microseconds'}
</code>
</pre>

Dans cet exemple :
- Toutes les broches ont les méthodes communes
- 3 broches pin3,pin4 et pin10 ont la méthode read_analog en plus.
- 3 broches pin0,pin1 et pin2 ont les méthodes read_analog et is_touched en plus.
- 13 broches pin7, pin6, pin5, pin20, pin8, pin9, pin13, pin12, pin11, pin16, pin15, pin14, pin19 ont la méthode get_analog_period_microseconds en plus.
