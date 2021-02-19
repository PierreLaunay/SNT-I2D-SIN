import microbit
valeur=microbit.pin2.read_analog()
lux=10**(valeur*4.74/1024)
print(lux)