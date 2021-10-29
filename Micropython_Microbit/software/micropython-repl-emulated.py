#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:10:08 2021
From python 3.8+
@author: pierre
"""
import re,serial,time,sys # bibliothèque à installer pyserial : pip install pyserial

parser = re.compile(r">>>(.+?)(?=>>>)",re.S)

    
# Appuyer sur le bouton reset de la carte Microbit avant de lancer
def envoyer_messages(messages) :
    for message in messages: ser.write(message) # on import la bibliothèque microbit, on récupère la liste des broches et leurs méthodes puis on l'affiche
    debut=time.time() #on initilaise le temps
    texte="" #on prendre un texte vide pour commencer
    while time.time()-debut < 1: #on récupère pendant 1 s les caractères reçus
        if ser.in_waiting : #caractère reçu ?
            texte+=ser.read(ser.in_waiting).decode("utf-8")#on le lit et on le transforme en utf8
            debut=time.time()
    return texte # on affiche le texte reçu

def reset():
    messages=[b'import microbit\r\n',b'microbit.reset()\r\n']
    envoyer_messages(messages)

def acquisition_messages(messages=[b'import microbit\r\n'],sortie='fin'):
    print("Écriture des commandes à envoyer à la carte Microbit")
    while (message:=input('>>> ')) !=sortie:
        messages.append((message+'\r\n').encode('utf-8'))
    return messages

try :
    ser=serial.Serial('/dev/ttyACM0') #ouvre le port du microbit
except serial.SerialException :
    print("vérifier que la carte Microbit est branchée sur le PC ou bien\nimport music !ls /dev/ttyA*")
    sys.exit()
ser.baudrate=115200 # le baudrate est à 115200 bauds par défaut
print(ser) #on affiche les infos du port série
reset()
messages_microbit=acquisition_messages()#([])
texte_reçu=envoyer_messages(messages_microbit)
if (matches:=parser.findall(texte_reçu)) != []:
    for match in matches:print(match)
ser.close()
