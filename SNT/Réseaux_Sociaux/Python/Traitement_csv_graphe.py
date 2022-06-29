#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:56:51 2022

@author: pierre
"""
import csv,pandas

with open("../graphonline/exemple1.csv") as file_name : array = list(csv.reader(file_name))
tableau=[[int(v) for v in l[1:]] for l in array[1:]] #pour enlever les noms des lignes et colonnes
df=pandas.DataFrame(tableau, index=array[0][1:], columns=array[0][1:])
somme = ['' for ligne in tableau] # on veut la somme de chaque ligne
dmax = ['' for ligne in tableau] # on veut la distance maximale pour chaque ligne
somme =[sum(ligne) for ligne in tableau] # on veut la somme de chaque ligne
dmax = [max(ligne) for ligne in tableau] # on veut la distance maximale pour chaque ligne
df["somme"]=somme
df["dist_max"]=dmax
print(df)
