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
