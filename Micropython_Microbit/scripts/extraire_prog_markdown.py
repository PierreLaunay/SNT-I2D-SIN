#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:42:43 2021
@author: pierre
"""
import re, pathlib
chemin = pathlib.Path.cwd().parent

def extraire(chemin,fichier,entete):
    texte=open(chemin.joinpath(fichier).as_posix(),'r').read()
    snippet = re.compile(r"```python\n#\s?((?:programme|exo).*?)\n(.*?)\n```",re.S)
    for titre,prog in snippet.findall(texte):
        nom=re.sub(" ","_",titre)
        f=open(chemin.joinpath(entete+nom+'.py').as_posix(),'w')
        f.write(prog)
        f.close()

extraire(chemin,"Microbit_interne.md","software/Interne_") 
extraire(chemin,"Microbit_externe.md","software/Externe_")
