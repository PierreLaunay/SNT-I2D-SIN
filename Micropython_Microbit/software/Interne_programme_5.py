import microbit
valeur = 0 # pour avoir la lampe éteinte
while True :
    if (microbit.button_b.get_presses() + microbit.button_a.get_presses())%2 == 1 :
        valeur = 9-valeur #valeur = 0 : led éteinte, valeur = 9 : led allumée
        # on inverse à chaque fois que l'un des boutons a changé d'état un nombre impair de fois
        microbit.display.set_pixel(2,2,valeur)