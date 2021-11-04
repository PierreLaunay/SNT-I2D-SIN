# Programmation Microbit MicroPython AP-IE08P

![Image microbit](../Images/microbit-front.png)

## Activité 8 - opérateurs logiques booléens

Matériel de base : 1 carte Microbit, un câble USB.
Pas de matériel spécifique, on utilisera le moniteur série dans l’IDE Mu ou en ligne https://python.microbit.org/v/2 avec Google Chrome


### Variables

2 entrées A, B booléennes.

8 sorties ET, OU, NONA, NONB, XOR, NAND, NOR, XNOR booléennes

Une variable n pour une boucle.

Partie avant le while True

Pour initialiser la liaison série on utilise : uart.init(baudrate=115200)

On n’a pas besoin d’initialiser la liaison série si on ne se sert que de la fonction print

baudrate: vitesse en bauds, nombre de bits transmis par seconde de 300 à 115200, valeur usuelle 115200.

Vous aurez plus d’informations sur https://microbit-micropython.readthedocs.io/en/v1.0.1/uart.html

Voici ce que l’on veut afficher :
print("Tables de vérité des fonctions NON A, NON B, OU, ET, XOR, NOR, NAND, XNOR")

Partie while True :
On veut afficher une table de vérité de 5 lignes, une ligne de titres et 4 lignes de valeur.

Aide de départ : pour faire les cas on va faire varier une variable n de 0 à 3 avec une boucle for
Les variables booléennes A et B seront réalisées à partir de cette variable n.

Pensez à regarder le cours sur "**Les opérateurs sur les bits CIE-11**"


Toutes les autres variables sont des des équations logiques de A et B.

Travail à réaliser : Écrire votre programme dans l’éditeur Mu ou en ligne  https://python.microbit.org/v/2 avec Google Chrome

Corrigez votre programme si nécessaire puis télécharger le dans la carte Microbit pour le tester sans oublier d’ouvrir le moniteur série.

####Travail à rendre : Rendre le programme avec des commentaires.

####Travail supplémentaire :

Réaliser un programme qui affiche la table de vérité de l’équation logique

S  = (/A + B) . (A + /B) . (/A + /B)

Remplacer   /A par ! A ;  + par or ; . par and pour faire une équation compatible au langage Micropython
Afficher la table de vérité de A, B et S.
