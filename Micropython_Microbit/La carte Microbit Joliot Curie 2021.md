La carte Microbit  Joliot Curie 2021
====================================

- [Présentation de la carte MICROBIT](#Présentation-de-la-carte-MICROBIT)
- [Comparaison ARDUINO  et MICROBIT](#Comparaison-des-cartes-de-développement-ARDUINO-et-MICROBIT)
- [Les outils logiciels pour travailler avec la carte MICROBIT](#Les-outils-logiciels-pour-travailler-avec-la-carte-MICROBIT)
- [Programme de base avec les ressources internes](#Programmes-de-base-avec-les-ressources-internes)
- [Capteurs externes et carte MicroBit](#Capteurs-externes-et-carte-MicroBit)

Présentation de la carte MICROBIT
----------------------------------

L'ensemble des ressources matérielles disponibles sur la carte BBC Micro:Bit

![Carte_microbit,40%](Hardware/microbit-overview-1-5.png)

Comparaison des cartes de développement ARDUINO et MICROBIT
------------------------------------------------------------

| |ARDUINO UNO |BBC:MICROBIT |
|--|--|--|
|Microcontrôleur|ATmega328P|ARM Cortex M0
|Architecture|8 bits|32 bits
Fréquence | 16 MHz|16 MHz
Mémoire Flash| 32 KB|256 KB
RAM | 2 KB|16 KB
EEPROM | 1 KB| -
Alimentation | 5 V| 3,3 V
Entrées/Sorties | 14 + 5| 19
CAN | 10 bits|10 bits
Bus série |I2C, SPI,UART,USB|I2C, SPI,UART,USB
**Capteurs/Actuateurs** |
Boutons poussoirs | - | 2
LEDs| 1 | 25 (matrice 5x5)
Accéléromètre| - | 1
Boussole| - | 1
Capteur de lumière| - |(avec les Leds)
Capteur de T°| - | T° du microcontrôleur (processor)
Antenne radio| - | 1
Programmation| C | Python
Documentation|Importante| Faible
Cartes additionnelles| Très variées| Beaucoup moins
Prix| ~ 20 € | ~ 20 €

Si vous voulez en savoir plus sur le
[hardware - matériel](Hardware/microbit_hardware_V1-5.md)

Les outils logiciels pour travailler avec la carte MICROBIT
-----------------------------------------------------------

Le logiciel de base pour les cartes Microbit est Microsoft MakeCode  
Il permet de travailler en bloc ou en javascript.

### Les outils logiciels pour travailler avec Micropython
1. Le logiciel Mu Editor pour MicroBit [https://codewith.mu/](https://codewith.mu/)  
Avec Mu, on peut télécharger sur la carte Microbit.  
On peut travailler en direct avec le mode REPL   \
REPL (session interactive en ligne de commande).  \
On peut télécharger des fichiers sur Microbit avec "Fichiers"
2. Le logiciel Jupyter Notebook permet aussi de travailler directement avec la carte MicroBit  \
Il faut installer Jupyter Notebook ou Anaconda puis installer **ubit_kernel** :
 * pip install ubit_kernel
 * python3 -m ubit_kernel.install  
[https://github.com/takluyver/ubit_kernel](https://github.com/takluyver/ubit_kernel)
3. Sous linux, on peut travailler avec un émulateur de terminal pour liaison série comme screen ou GtkTerm
[https://github.com/Jeija/gtkterm](https://github.com/Jeija/gtkterm)  
ou dans un terminal : screen /dev/ttyACM0 115200

### Les outils en ligne
1. Programmer en python la carte Microbit [https://python.microbit.org/v/2](https://python.microbit.org/v/2)
2. Vittascience : [https://fr.vittascience.com/microbit/?mode=mixed&console=bottom](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom)  
On peut travailler avec des blocs ou en python.  
Ce logiciel permet de télécharger, mais aussi de **simuler**  
Si on veut travailler avec la liaison série, on prend le navigateur Chrome.
3. Edublocks  [https://app.edublocks.org/](https://app.edublocks.org/)  
Permet de travailler avec des blocs ou en Python
4. Un simulateur python :  [https://create.withcode.uk/](https://create.withcode.uk/)

### Vittascience

Voici 2 documents pour travailler avec des blocs et en Micropython qui ont été faits avec un collègue du lycée Joliot-Curie à Rennes pour des élèves de seconde en SNT.

[bloc_python1]("Vittascience/Bloc_Python_Microbit.pdf)

[bloc_python2](Vittascience/Bloc_Python_Microbit2.pdf)

Programmes de base avec les ressources internes
--------------------------------------------

[Programmation de base de la carte Microbit](Microbit_interne.md)

Capteurs externes et carte MicroBit
-----------------------------------

[Utilisation de capteurs externes avec la carte Microbit ](Microbit_externe.md)
