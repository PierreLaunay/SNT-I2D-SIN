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
    def __init__(self, fenetre, Noms,table,boucle):
        tkinter.Frame.__init__(self, fenetre)
        self.noms = Noms
        self.numberLines = len(table)+1
        self.numberColumns = len(Noms)
        self.table = table
        self.pack(fill=tkinter.BOTH)
        self.nb=max([len(n) for n in self.noms])# nombre caractère max des noms
        self.remplir_entete(0,1)  #colonne noms
        self.remplir_entete(1,0) # ligne noms
        self.remplir() # contenu tableau
        if boucle :
            bouton = tkinter.Button(self,text="Remplir puis Valider",command=self.stock)
            bouton.grid(row=self.numberLines,columnspan=self.numberColumns)

    def entree(self,v,x,y):
            cell = tkinter.Entry(self)
            cell.configure(width=self.nb)
            cell.insert(0,v) # cell.insert(0,self.noms[i])
            cell.grid(row = x, column = y) # cell.grid(row = r*i, column = c*i)
            return cell
    def remplir_entete(self,r,c):#affichage noms ligne,colonne
        for i in range(self.numberColumns): self.entree(self.noms[i],r*i,c*i)
    def remplir(self): # remplissage table
        self.data = [[self.entree(self.table[i][j],i+1,j+1) for j in range(self.numberColumns-1)] for i in range(self.numberLines-1)]
    def stock(self):
        self.grille=[[colonne.get() for colonne in ligne] for ligne in self.data]
        self.liaison = [(self.noms[i+1],self.noms[j+1]) for i,ligne in enumerate(self.data) for j,colonne in enumerate(ligne) if colonne.get() != '0']
        for element in self.noms[1:] : G.add_node(element)
        for ligne in self.liaison : G.add_edge(*ligne)
        x=nx.floyd_warshall(G)
        self.tableau=[[int(x[l][m]) for m in self.noms[1:]] for l in self.noms[1:]]
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        sl=['somme' for ligne in self.tableau]# somme de chaque ligne à modifier
        maxl=['max' for ligne in self.tableau]# distance maximale de chaque ligne à modifier
        self.tableau.append(sl) # vrai si tableau symétrique uniquement sinon sc=[sum(c) for c in zip(*table1)]
        self.tableau.append(maxl)# vrai si tableau symétrique uniquement sinon maxc = [max(c) for c in zip(*table1)]
        self.resultats = IHM(tkinter.Tk(), self.noms,self.tableau,False)
# Début du programme
anv=['','Alban','Béatrice','Charles','Déborah','Éric','Fatima','Gérard','Hélène']
taol=[(len(anv)-1)*[0]]*(len(anv)-1) #vide
taol1=[[0]+[1]*(len(anv)-2)]+[(len(anv)-1)*[0]]*(len(anv)-2) #pour test
interface = IHM(tkinter.Tk(),anv,taol1,True)
interface.mainloop()
