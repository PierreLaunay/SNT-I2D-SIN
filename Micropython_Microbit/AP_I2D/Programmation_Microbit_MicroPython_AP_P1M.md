# Programmation Microbit MicroPython AP_P1M

![Image microbit](../Images/microbit-front.png)

## Activité 1 – Led et délais

Prérequis :
    • Cours programmation algorigramme : CP-1 et CP-2
    • Cours programmation C : CP-C01, CP-C02, CP-C03 et CP-C04

Description de l’application :

Commander l’allumage ou l’extinction d’une Led rouge avec des délais à l’aide d’un programme implanté dans la carte Microbit.

Matériel et montage :

    • Une carte Microbit.
    • Un câble USB pour relier la carte Microbit au PC.

Algorigramme de l’application :
L’algorigramme suivant décrit le fonctionnement de l’application et permet l’élaboration d’un programme avec les logiciels suivants :

Programme Micropython pour Microbit

Question 1 :
    a) Editer le programme suivant sous https://python.microbit.org/v/2 avec Google Chrome  (sans oublier de le sauvegarder) avant de le téléverser pour vérifier son bon fonctionnement :

<div style="display: flex">
    <div class="left">
    <div style="margin: 1em 0 0 0; background-color:lightgrey; padding: 0.5em 10em 12em 0.5em;"> 
<p style="margin: 1em 0 0 0;"> from microbit import *</p>
<p style="margin: 4em 0 0 0;"> while True:</p>
<p style="margin: 5em 0 0 2em;"> display.set_pixel(2,2,9)</p>
<p style="margin: 4em 0 0 2em;"> sleep(500)</p>
<p style="margin: 3em 0 0 2em;"> display.set_pixel(2,2,0)</p>
<p style="margin: 4em 0 0 2em;"> sleep(1000)</p>
   </div>
    </div>
    <div class="right">
      <img src="../Images/algo_clignotant.svg">
    </div>
</div>



    b) Dans le document réponse, indiquer le lien (par des flèches) entre l’algorithme de l’application et le programme micropython Microbit.
