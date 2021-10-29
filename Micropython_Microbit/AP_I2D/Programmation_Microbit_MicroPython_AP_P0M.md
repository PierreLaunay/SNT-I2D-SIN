# Programmation Microbit MicroPython AP_P0M

![Image microbit](../Images/microbit-front.png)

## Activité 0 - Initiation à Micropython sur MicroBit

- Description de l’application :
Commander l’allumage ou l’extinction d’une Led rouge à l’aide d’un programme implanté dans la carte Microbit avec le langage MicroPython.

### Matériel et montage :

    • Une carte Microbit
    • Un câble USB pour relier la carte Microbit au PC.

### Pour programmer :

    • En ligne avec  https://python.microbit.org/v/2 avec Google Chrome
    • ou bien Mu s’il est installé sur le PC

### Travail à rendre
Travail vous devez sauvegarder tous vos tests avec des commentaires dans un document texte et l’imprimer une fois l’activité terminée.

## TEST0

<pre>
<code>
from microbit import *
while True : # Boucle sans fin
	#la ligne commence par une tabulation
	display.set_pixel(0, 0, 9) # pour allumer (9) la LED à la position 0,0
	sleep(1000) # attendre 1s (1000 ms)
	display.set_pixel(0, 0, 0) # pour éteindre (9) la LED à la position 0,0
	sleep(1000) # attendre 1s (1000 ms)
  </code>
  </pre>

    • Écrivez ce programme Micropython sur https://python.microbit.org/v/2  avec Google Chrome
    • Branchez votre carte Microbit et connectez la (Connect)
    • téléversez (download) pour vérifier son bon fonctionnement.
    • Sauvegarder le programme en python Load/Save → Save : Download Python Script

## TEST1

Modifiez le test1 pour que la LED centrale s’allume

Vous pouvez lire l’aide : https://microbit-micropython.readthedocs.io/fr/latest/display.html

**Important** : n’oubliez pas de sauvegarder avec un nom différent chaque programme python !

## TEST2

<pre>
<code>
from microbit import *
while True :
	display.set_pixel(0, 0, 9)
	sleep(100)
	display.set_pixel(0, 0, 0)
	sleep(300)
	display.set_pixel(0, 0, 9)
	sleep(1)
	display.set_pixel(0, 0, 0)
	sleep(2000)
</code>
</pre>

- Écrivez ce programme sur https://python.microbit.org/v/2  puis téléverser sur la carte Microbit pour vérifier son fonctionnement.
- Il faut commenter le programme.
- N’oubliez pas de sauvegarder le programme.

## TEST3

<pre>
<code>
from microbit import *
while True :
	display.set_pixel(0, 0, 0)
	sleep(1000)
	display.set_pixel(0, 0, 1)
	sleep(1000)
	display.set_pixel(0, 0, 2)
	sleep(1000)
	display.set_pixel(0, 0, 3)
	sleep(1000)
	display.set_pixel(0, 0, 4)
	sleep(1000)
	display.set_pixel(0, 0, 5)
	sleep(1000)
	display.set_pixel(0, 0, 6)
	sleep(1000)
	display.set_pixel(0, 0, 7)
	sleep(1000)
	display.set_pixel(0, 0, 8)
	sleep(1000)
	display.set_pixel(0, 0, 9)
	sleep(1000)
</code>
</pre>

- Écrivez ce programme sur https://python.microbit.org/v/2  puis téléverser sur la carte Microbit pour vérifier son fonctionnement.
- Il faut commenter le programme.
- N’oubliez pas de sauvegarder le programme.

Que fait ce programme ?

## TEST4

<pre>
<code>
from microbit import *
while True :
	for i in range(10) :
		display.set_pixel(0, 0, i)
		sleep(1000)
</code>
</pre>

- Écrivez ce programme sur https://python.microbit.org/v/2  puis téléverser sur la carte Microbit pour vérifier son fonctionnement.
- Il faut commenter le programme.
- N’oubliez pas de sauvegarder le programme.
- Quelles différences avec le programme précédent ?

### Extra

Découvrons la boucle for

## TEST5

<pre>
<code>
from microbit import *
while True :
	for i in range(5) :
		display.set_pixel(i, 0, 9)
		sleep(1000)
		display.set_pixel(i, 0, 0)
		sleep(1000)
</code>
</pre>

- Quelles sont les valeurs que peut prendre i ?
- Écrivez ce programme sur https://python.microbit.org/v/2  puis téléverser sur la carte Microbit pour vérifier son fonctionnement.
- Il faut commenter le programme.
- N’oubliez pas de sauvegarder le programme.

Que fait ce programme ?

## TEST6
Proposez un programme qui allume les LED verticalement sur une colonne à partir du programme précédent.

Programmer, tester, sauvegarder.

## TEST7
Proposez un programme qui allume les LED horizontalement et verticalement.

Il faudra utiliser 2 boucles for imbriquées avec 2 variable i et j

Programmer, tester, sauvegarder.

## TEST8

<pre>
<code>
from microbit import *
while True :
    for j in range(5):
        for i in range(5):
            display.set_pixel(i, j, i+j)
            sleep(1000)
</code>
</pre>

Programmer, tester, sauvegarder.

Que fait ce programme ?

Quelle est la luminosité de la LED en bas à droite ?

[Activité 1 – Led et délais](Programmation_Microbit_MicroPython_AP_P1M)
