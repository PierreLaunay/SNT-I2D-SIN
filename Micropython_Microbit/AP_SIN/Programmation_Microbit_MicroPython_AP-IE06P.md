# Programmation Microbit MicroPython AP-IE06P

![Image microbit](../Images/microbit-front.png)

## Activité 6 - boucle for

 Boucle for et affichage console.
Le but de cette activité est de mettre en œuvre la boucle for. Pour cela on utilisera les 25 LEDS

Matériel : Une carte Microbit


Structure du programme à compléter :

<pre>
<code>
//-------------------------------------
// AP-IE06 Programmation de base
// Boucle for et afficheur LCD
//
// Nom :
// Date :
//-------------------------------------
from microbit import *

while True :
# Faire une boucle pour l’axe y
# Faire une boucle imbriquée pour l’axe x
# Pour l’affichage la fonction  display.set_pixel(x, y, value)

</pre>
</code>

Que doit faire le programme ?

Fonction while True :
    1. Afficher les LED une à une dans l’axe x puis dans l’axe y

Pour faire les boucles, il faut utiliser la fonction range() dans le For
Vous pouvez utiliser le logiciel Edupython pour faire des essais avec la fonction range.

Travail demandé :
1°) version 1 :  Le programme affichera les LEDs une à une dans l’axe x puis y

2°) version 2 : Faire une version où la led s’allume pendant 200 ms puis la seconde 200 ms et ainsi de suite
	Pour faire une pause on utilisera la fonction 	sleep() qui est en millisecondes.

3) version 3 : Faire un serpentin comme ceci :

* * * * *  sens →
        *
* * * * * sens ←
*
* * * * * sens →

Vous pourrez voir sur Edupython comment faire un range avec un pas négatif . [Edupython bases](https://download.tuxfamily.org/edupython/Bases.pdf)

Vous pouvez utiliser aussi le modulo , noté % en python

N’oubliez pas de commenter vos programmes et de les imprimer avant de rendre cette activité.
