# Programmation Microbit MicroPython AP-IE07P

![Image microbit](../Images/microbit-front.png)

## Activité 7 - contrôle itératif While et le moniteur série

Matériel de base : 1 carte Microbit, un câble USB.
Pas de matériel spécifique, on utilisera le moniteur série dans l’IDE Mu ou en ligne https://python.microbit.org/v/2 avec Google Chrome

Programme : Démarrage d’un programme sur un évènement

Variables : Aucune

Partie avant le while True

Pour initialiser la liaison série on utilise : uart.init(baudrate=115200)

On n’a pas besoin d’initialiser la liaison série si on ne se sert que de la fonction print

baudrate: vitesse en bauds, nombre de bits transmis par seconde de 300 à 115200, valeur usuelle 115200.

Vous aurez plus d’informations sur https://microbit-micropython.readthedocs.io/en/v1.0.1/uart.html

On affiche un message pour informer l’utilisateur
print("Taper une touche quelconque  pour démarrer le programme")

Partie while True:
On attend de recevoir un caractère de la liaision série.
Lire https://microbit-micropython.readthedocs.io/fr/latest/uart.html , remarque en Français (fr) ou anglais (en) la documentation spécialisée reste en anglais !

<pre>
<code>
if microbit.uart.any() :  # que réalise cette ligne ?
	print("programme démarre")  # on pourra remplacer par un sous-programme et lancer un programme sur la frappe d’une touche ou d’un BP ...
# fin de la boucle while True
</code>
</pre>

Écrire votre programme dans l’éditeur Mu ou en ligne et lancer la compilation, corriger si nécessaire puis télécharger votre programme dans la carte et tester, n’oublier pas d’ouvrir le moniteur série.

Variante avec une touche spécifique ‘D’

<pre>
<code>
if microbit.uart.any() :
	 c = uart.read()
	 d = str(c,'utf-8')
	 print(c,d)
	 if (d == ’D’) :
	     print("programme démarre")
</code>
</pre>

Au lieu de print, on peut utiliser uart.write(buf) mais attention, il faut envoyer une liste de caractères !

On évite de mettre un while dans un while True !

Travail à rendre : Rendre les deux programmes avec des commentaires.
