import microbit
while True :
    if microbit.button_b.is_pressed(): # bouton b : Marche
        microbit.display.set_pixel(2,2,9)
    if microbit.button_a.is_pressed(): # bouton a : Arrêt
        microbit.display.set_pixel(2,2,0)