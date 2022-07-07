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
    def __init__(self, fenetre, Noms,table,boucle, **kwargs):
        tkinter.Frame.__init__(self, fenetre)
        self.noms = Noms
        self.numberLines = len(table)+1
        self.numberColumns = len(Noms)
        self.table = table
        self.pack(fill=tkinter.BOTH)
        self.nb=max([len(n) for n in self.noms])# nombre caractère max des noms
        self.parametres = kwargs if kwargs else {}
        for i in range(self.numberColumns): #affichage noms colonne
            cell = tkinter.Entry(self)
            cell.configure(width=self.nb)
            cell.insert(0,self.noms[i])
            cell.grid(row = 0, column = i)

        for i in range(self.numberColumns): #affichage noms ligne
            cell = tkinter.Entry(self)
            if self.parametres and i-1 in self.parametres.get("centre"):
                cell.configure(width=self.nb, background=self.parametres.get("couleur")[0])
            else : cell.configure(width=self.nb)
            cell.insert(0,self.noms[i])
            cell.grid(row = i, column = 0)

        self.data = list()
        for i in range(self.numberLines-1): # remplissage table
            line = list()
            for j in range(self.numberColumns-1):
                valeur = self.table[i][j]
                cell = tkinter.Entry(self)
                if self.parametres and i==self.numberLines-2:
                    if valeur == self.parametres.get("rayon"):
                        cell.configure(width=self.nb, background = self.parametres.get("couleur")[2])
                    if valeur == self.parametres.get("diametre"):
                        cell.configure(width=self.nb, background = self.parametres.get("couleur")[1])
                else : cell.configure(width=self.nb)
                cell.insert(0, valeur)
                line.append(cell)
                cell.grid(row = i+1, column = j+1)
            self.data.append(line)

        if boucle :
            cell=tkinter.Button(self,text="Valider",command=self.stock)
            cell.grid(row=self.numberLines,column=self.numberColumns//2)

    def stock(self):
        self.grille=[[colonne.get() for colonne in ligne] for ligne in self.data]
        self.liaison = [(self.noms[i+1],self.noms[j+1])
                        for i,ligne in enumerate(self.data)
                        for j,colonne in enumerate(ligne)
                        if colonne.get() != '0']
        for element in self.noms[1:] : G.add_node(element)
        for ligne in self.liaison : G.add_edge(*ligne)   # x,y=ligne
        x=nx.floyd_warshall(G)
        self.tableau=[[int(x[l][m]) for m in self.noms[1:]] for l in self.noms[1:]]
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        sl=[sum(ligne) for ligne in self.tableau]# somme de chaque ligne
        maxl=[max(ligne) for ligne in self.tableau]# distance maximale de chaque ligne
        sml={(s,m):[i for ((i,s1),m1) in zip(enumerate(sl),maxl) if s==s1 and m==m1] for ((i,s),m) in zip(enumerate(sl),maxl)}
        self.centre = sml[min(sml)]
        self.rayon=min(sml)[1]
        self.diametre=max(sml)[1]
        for i in self.centre: print("centre :",self.noms[i+1]) #attention '0' vide dans noms
        print("rayon",self.rayon,", diamètre",self.diametre)
        self.tableau.append(sl) # vrai si tableau symétrique uniquement sinon sc=[sum(c) for c in zip(*table1)]
        self.tableau.append(maxl)# vrai si tableau symétrique uniquement sinon maxc = [max(c) for c in zip(*table1)]
        self.resultats = IHM(tkinter.Tk(), self.noms,self.tableau,False, couleur=["#ff9977", "#22ff88", "#ffff22"], centre=self.centre, rayon=self.rayon, diametre=self.diametre)
        #print(self.tableau)
# Début du programme
anv=['','Alban','Béatrice','Charles','Déborah','Éric','Fatima','Gérard','Hélène']
taol=[(len(anv)-1)*[0]]*(len(anv)-1) #vide
taol1=[[0]+[1]*(len(anv)-2)]+[(len(anv)-1)*[0]]*(len(anv)-2) #pour test
fenetre = tkinter.Tk()
interface = IHM(fenetre, anv,taol1,True)
interface.mainloop()
