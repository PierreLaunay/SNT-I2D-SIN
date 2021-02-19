import microbit # bibliothèque nécessaire pour travailler avec la carte microbit
microbit.display.clear() # on efface les leds

while True :
    if microbit.button_a.is_pressed():
        microbit.display.set_pixel(2,2,9)