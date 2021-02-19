# version profs avec une liste
import microbit
Rosace_vents=[fleche_N,fleche_N_E,fleche_E,fleche_S_E,fleche_S,fleche_S_O,fleche_O,fleche_N_O] #liste pour profs
while True:
    aiguille = (225-10 * microbit.compass.heading())%3600 // 450
    microbit.display.show(Rosace_vents[aiguille]) # utilisation d'une liste