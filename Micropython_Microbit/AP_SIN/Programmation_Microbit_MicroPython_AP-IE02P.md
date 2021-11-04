# Programmation Microbit MicroPython AP-IE02P

![Image microbit](../Images/microbit-front.png)

## Activité 2 – structure de contrôle if else

Structure de contrôle if else et les entrées/sorties

Le but de cette activité est de comprendre comment on peut lire l'état d'un BP bouton poussoir, faire un choix selon cet état (0 ou 1) et modifier l'état d'une sortie LED.

Matériel : Une carte Microbit suffira puisqu’on utilisera un bouton poussoir et une LED internes à la carte.

Structure du programme à compléter :

<pre>
<code>
#----------------------------------
# AP-IE02 Programmation de base
# Contrôle if else et entrées/sorties
#
# Nom :
# Date :
#----------------------------------

# Add your Python code here. E.g.
from microbit import * # on importe la bibliothèque microbit qui gère le matériel (hardware)
</code>
</pre>

- Le bouton A se nomme : **button_a**
- Pour allumer une led on utilise **display.set_pixel(x, y, value)** x et y indique la position de la LED et value indique la luminosité comprise entre 0(éteinte) et 9(pleine puissance)

Pas de configuration des entrées et sorties internes (sur la carte) en micropython

<pre>
<code>
while True :
    # on lit l'état du BP avec la fonction is_pressed()

    etat_bp =

    # si le BP est actionné, on allume une LED avec la fonction display.set_pixel(x, y, value)
    if (. . . . . . . . ) :
        . . . . . . . . . . .

</code>
</pre>

Que doit faire le programme ? Après avoir configuré les entrées/sorties, la LED devra être éteinte, elle devra s'allumer si on appuie sur le bouton poussoir et s'éteindre si on relâche de bouton poussoir

Pour obtenir de l'aide sur les fonctions is_pressed(), display,set_pixel( et sur la structure de contrôle if, allez sur les pages https://microbit-micropython.readthedocs.io/fr/latest/

Pour programmer :
    • En ligne avec  https://python.microbit.org/v/2 avec Google Chrome
    • ou bien Mu s’il est installé sur le PC

On allumera la LED au centre de la matrice de LEDs

# VERSION 1 : Sans "else" 
Dans une première version, on n'utilisera pas le mot clé else, deux tests (if) seront nécessaires.

Exercice 1 : Donnez l’algorigramme de la fonction while True

Réponses :
<br>
<br>
<br>
<br>

Exercice 2 : Complétez le programme et testez-le.

# VERSION 2 : Avec "else" 
Dans une deuxième version, on utilisera le mot clé else, un seul test est nécessaire.

Exercice 3 : Donnez l’algorigramme de la fonction while True

Réponses :
<br>
<br>
<br>
<br>

Exercice 4 : Complétez le programme et testez-le.

Conclusion :
<br>
<br>

Documents à rendre à la fin de la séance :
    • Ce document complété.
    • Les deux programmes imprimés.

**EXTRA :**

On peut simuler son programme à la maison sans carte Microbit sue le site https://create.withcode.uk/

Pour faire des algorigrammes, on peut utiliser :
- [Diagram.drawio](https://app.diagrams.net/)
- En python la bibliothèque [schemdraw](https://schemdraw.readthedocs.io/en/latest/)
