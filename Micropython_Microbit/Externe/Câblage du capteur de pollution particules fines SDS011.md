Câblage du capteur de pollution particules fines SDS011
=======================================================

Branchement VCC au 5 V d'une carte Arduino par exemple
Branchement GND à la carte Arduino
Branchement GND entre carte Arduino et l'interface Kitronik pour MicroBit
Branchement TxD à la borne 1 de l'interface Kitronik pour MicroBit
Dans Particules_fines.py : microbit.uart.init(baudrate=9600,tx = microbit.pin0, rx = microbit.pin1)

Mettre le programme Particules_fines.py dans la carte Microbit avec Mu
Vérifier avec REPL de Mu que les trames arrivent bien.
Enlever REPL puis éteindre Mu

Ouvrir Jupyter Notebook
Ouvrir le fichier PMSensor_pyplot.ipynb
Exécuter les différentes cellules python
Vous aurez une courbe en temps réel des polluants PM2.5 et PM10 en fonction du temps.

Voici les limites à ne pas dépasser.
-------------------------------------

Particules fines de diamètre inférieur ou égal à 10 micromètres (PM10)  
En moyenne annuelle : depuis le 01/01/05 : 40 µg/m³. Objectif : 30µg/m³  
En moyenne journalière : depuis le 01/01/2005 : 50 µg/m³ à ne pas dépasser plus de 35 jours par an.

Particules fines de diamètre inférieur ou égal à 2,5 micromètres (PM2,5)  
En moyenne annuelle : 25 µg/m³ depuis le 01/01/15. Objectif : 10µg/m³

[https://www.airparif.asso.fr/reglementation/normes-francaises](https://www.airparif.asso.fr/reglementation/normes-francaises)

[https://www.airparif.asso.fr/_pdf/arrete-19042017.pdf](https://www.airparif.asso.fr/_pdf/arrete-19042017.pdf)
