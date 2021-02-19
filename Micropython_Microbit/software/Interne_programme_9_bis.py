import microbit
fleche_N = microbit.Image("00900:00900:00900:00000:00000")
fleche_N_E = microbit.Image("00009:00090:00900:00000:00000")
fleche_E = microbit.Image("00000:00000:00999:00000:00000")
fleche_S_E = microbit.Image("00000:00000:00900:00090:00009")
fleche_S = microbit.Image("00000:00000:00900:00900:00900")
fleche_S_O = microbit.Image("00000:00000:00900:09000:90000")
fleche_O = microbit.Image("00000:00000:99900:00000:00000")
fleche_N_O = microbit.Image("90000:09000:00900:00000:00000")
while True:
    if microbit.button_a.is_pressed(): #appuyer sur le bouton A pour sortir du programme
        break
    aiguille = (225-10 * microbit.compass.heading())%3600 // 450
    if aiguille == 0 :
        microbit.display.show(fleche_N)
    elif aiguille == 1 :
        microbit.display.show(fleche_N_E)
    elif aiguille == 2 :
        microbit.display.show(fleche_E)
    elif aiguille == 3 :
        microbit.display.show(fleche_S_E)
    elif aiguille == 4 :
        microbit.display.show(fleche_S)
    elif aiguille == 5 :
        microbit.display.show(fleche_S_O)
    elif aiguille == 6 :
        microbit.display.show(fleche_O)
    elif aiguille == 7 :
        microbit.display.show(fleche_N_O)
    else :
        microbit.display.show("99999:09990:00900:09990:99999") # erreur