import microbit
while True :
    if microbit.button_a.is_pressed(): # bouton appuyé ?
        microbit.display.set_pixel(2,2,9)
    else :
        microbit.display.set_pixel(2,2,0)