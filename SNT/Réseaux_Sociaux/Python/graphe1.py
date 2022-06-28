#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:23:36 2022

@author: pierre
"""

import tkinter
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()  #G=nx.DiGraph() Graph non directionnel, DiGraph directionnel

class IHM(tkinter.Frame) : # class IHM(Frame)
    def __init__(self, fenetre, Noms):
        tkinter.Frame.__init__(self, fenetre)
        self.noms = Noms
        self.numberLines = len(Noms)
        self.numberColumns = len(Noms)
        self.pack(fill=tkinter.BOTH)

        for i in range(self.numberColumns):
            cell = tkinter.Entry(self)
            cell.insert(0,self.noms[i])
            cell.grid(row = 0, column = i)

        for i in range(self.numberColumns):
            cell = tkinter.Entry(self)
            cell.insert(0,self.noms[i])
            cell.grid(row = i, column = 0)

        self.data = list()
        for i in range(self.numberLines-1):
            line = list()
            for j in range(self.numberColumns-1):
                cell = tkinter.Entry(self)
                cell.insert(0, 0)
                line.append(cell)
                cell.grid(row = i+1, column = j+1)
            self.data.append(line)
        cell=tkinter.Button(self,text="Valider",command=self.stock)
        cell.grid(row=self.numberLines,column=self.numberColumns//2)

    def stock(self):
        self.grille=[[colonne.get() for colonne in ligne] for ligne in self.data]
        self.liaison = [(self.noms[i+1],self.noms[j+1])
                        for i,ligne in enumerate(self.data)
                        for j,colonne in enumerate(ligne)
                        if colonne.get() != '0']
        for element in self.noms[1:] : G.add_node(element)
        for ligne in self.liaison :
            x,y=ligne
            G.add_edge(x,y)
        x=nx.floyd_warshall(G)
        self.tableau=[[x[l][m] for m in self.noms[1:]] for l in self.noms[1:]]
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        print(self.tableau)
        sl=[sum(ligne) for ligne in self.tableau]
        centre=sl.index(min(sl))
        rayon=max(self.tableau[centre])
        diametre=max(self.tableau[sl.index(max(sl))])
        print("centre",centre,", rayon",rayon,", diamètre",diametre)
# Début du programme
anv=['','Alban','Béatrice','Charles','Déborah','Éric','Fatima','Gérard','Hélène']
fenetre = tkinter.Tk()
interface = IHM(fenetre, anv)
interface.mainloop()
