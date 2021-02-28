#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:48:07 2021

@author: pierre
"""
import pathlib
chemin = pathlib.Path.cwd().parent
nom="software/liste_programmes"
programmes=list(chemin.glob('software/*.py'))
f=open(chemin.joinpath(nom+'.md').as_posix(),'w')
f.write('# Listes des programmes Micropython pour Microbit\n\n')
for p in programmes : f.write('['+p.name+']('+p.name+')\n\n')
f.close()
