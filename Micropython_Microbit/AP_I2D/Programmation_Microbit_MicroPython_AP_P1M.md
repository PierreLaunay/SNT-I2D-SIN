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

<div>
    <img src="../Images/algo_clignotant.svg" align="right">
    <div>
        <p > from microbit import *</p>
        <br>
        <br>
        <br>
        <p > while True:</p>
        <blockquote>
            <br>
            <br>
            <br>
            <br>
            <p><b>display.set_pixel(2,2,9)</b></p>
            <br>
            <br>
            <p ><b> sleep(500)</b></p>
            <br>
            <br>
            <p ><b> display.set_pixel(2,2,0)</b></p>
            <br>
            <br>
            <p ><b> sleep(1000)</b></p>
        </blockquote>
    </div>
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
b) Dans le document réponse, indiquer le lien (par des flèches) entre l’algorithme de l’application et le programme micropython Microbit.
