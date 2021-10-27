modules=['sys','os','gc','utime','micropython','microbit','machine','radio','array','builtins','ucollections','math','random','ustruct','audio','speech','music','neopixel','love','this','antigravity']
# extrait de help('microbit') après avoir enlevé les doubles, les modules sont en fait les bibliothèques    
def aide(nom): #fonction avec un paramètre de bibliothèque
    print(nom)  # affiche le nom du module
    print(help(eval(nom))) # affiche l'aide sur la bibliothèque
    for m in dir(eval(nom)): # on liste les fonctions d'une bibliothèque
        print(nom+'.'+m) # on obtient le module.la fonction comme microbit.button_a
        if ( type(eval(nom+'.'+m)) != str) : help(eval(nom+'.'+m))# on n'affiche pas les fonctions attributs comme name par exemple
    print("--------------------") # mais on affiche l'aide sur la fonction de la bibliothèque
    print(gc.mem_free()) #on affiche la mémoire libre
    gc.collect() # pour libérer de l'espace mémoire (garbage collection)

for nom in modules : # prendre un nom parmi les bibliothèques
    exec("import {module}".format(module=nom)) # pour installer la bibliothèque
    print(nom) #on affiche le nom de la bibliothèque installée
print(gc.mem_free()) # on affiche la mémoire libre
gc.collect() # pour libérer de l'espace mémoire (garbage collection)
for nom in modules : # prendre un nom parmi les bibliothèques
    aide(nom) # on affiche, la bibliothèque et l'aide sur la bibliothèque et l'aide sur ses fonctions

print("__________Fin Module___________")

info = {i:dir(globals()[i]) for i in globals()} # on crée 1 dico avec tous les noms globaux et leurs fonctions
for i,j in info.items() : print(i,j) # on affiche le dictionnaire
print("--------------------")
print(gc.mem_free())  # on affiche la mémoire libre
gc.collect()                # pour libérer de l'espace mémoire (garbage collection)
aide('microbit.button_a')   # pour avoir l'aide sur le bouton A et ses fonctions
aide('microbit.display')    # pour avoir l'aide sur l'afficheur et ses fonctions
aide('microbit.pin0')       # pour avoir l'aide sur la broche 0 et ses fonctions (les autres pins sont proches)
aide('microbit.uart')       # pour avoir l'aide sur l'uart (liasion série) et ses fonctions
aide('microbit.spi')        # pour avoir l'aide sur le bus spi et ses fonctions
aide('microbit.i2c')        # pour avoir l'aide sur le bus i2c et ses fonctions
aide('microbit.compass')    # pour avoir l'aide sur la boussole et ses fonctions
aide('microbit.accelerometer')  # pour avoir l'aide sur l'accéléromètre et ses fonctions
aide('microbit.temperature')    # pour avoir l'aide sur le capteur de température et ses fonctions
pins=sorted([i for i in info['microbit'] if i.startswith("pin")], key=lambda x: int(x[3:])) #on trie les broches 
# par ordre numérique, le tri se fait avec key on enlève pin avec x[3:] tri par nombre avec int pour ne pas avoir 10..19 entre 1 et 2
print("pins",pins) # on affiche la liste des broches
print(gc.mem_free()) 
gc.collect()
images=sorted([ i for i in dir(microbit.Image) if i[0].isupper()]) # on ne garde que les noms qui commencent par 1 majuscule
print("images",images) # affichage de la liste des images 
