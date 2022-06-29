#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:51:55 2022.

@author: tanguy
"""
import pandas
from bs4 import BeautifulSoup as bs
from dataclasses import dataclass
import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg

@dataclass
class Node:
    """Graph node."""

    id: int
    maintext: str
    x: float
    y: float
    size: int
    uptext: str

@dataclass
class Edge:
    """Graph Edge."""

    id: int
    isdirect: bool
    model_value: float
    model_type: int
    model_width: int
    source: int
    target: int
    text: str
    uptext: str
    weight: int

@dataclass
class Graph:
    """Graph system."""

    nodes: list
    edges: list
    idbased: bool
    namebased: bool

    def make_graph(self):
        """
        Create a dictionary with nodes and vertices.

        Returns
        -------
        Dict
            DESCRIPTION.

        """
        if self.idbased:
            self.graph = {
                "nodes": [n.id for n in self.nodes],
                "vertices": [(e.source, e.target) for e in self.edges],
            }
        if self.namebased:
            self.named_nodes = {n.id: n.maintext for n in self.nodes}
            self.graph = {
                "nodes": [n.maintext for n in self.nodes],
                "vertices": [
                    (self.named_nodes.get(e.source), self.named_nodes.get(e.target))
                    for e in self.edges
                ],
            }
        return self.graph

def nodes(data) :
    Nodes = [
        Node(
            id=int(n.get("id")),
            maintext=n.get("mainText"),
            x=float(n.get("positionX")),
            y=float(n.get("positionY")),
            size=int(n.get("size")),
            uptext=n.get("upText"),
        )
        for n in data.select("node")
    ]
    return Nodes
def edges(data) :
    Edges = [
        Edge(
            id=int(e.get("id")),
            model_value=float(e.get("model_curvedValue")),
            model_type=int(e.get("model_type")),
            model_width=int(e.get("model_width")),
            isdirect=bool(e.get("isDirect")),
            source=int(e.get("source")),
            target=int(e.get("target")),
            text=e.get("text"),
            uptext=e.get("uptext"),
            weight=int(e.get("weight")),
        )
        for e in data.select("edge")
    ]
    return Edges

###########################################

sg.theme("DarkTeal2")
layout = [[sg.Text("Choisir un fichier grahml: "), sg.Input(), sg.FileBrowse("Parcourir",key="-IN-")],[sg.Button("Valider")]]

### Afficher une fenêtre pour choisir le fichier graphml
window = sg.Window('Mon navigateur de fichiers', layout, size=(600,150))

while True: #boucle sans fin, on sort avec les break
    event, values = window.read() # pour lire les paramètres passés
    if event == sg.WIN_CLOSED : # pour sortir directement
        window.close() # on ferme la fenêtre
        break #on sort de la la boucle sans fin
    elif event == "Valider": # une fois le fichier choisi, on valide
        fichier=values["-IN-"] # sauvegarde du fichier graphml dans fichier
        print(values["-IN-"]) # on affiche le nom du fichier
        window.close() # on ferme la fenêtre
        break #on sort de la la boucle sans fin
###
with open(fichier, "r") as f: file = f.read() #lecture du fichier graphml
donnees = bs(file, features="xml") #fichier de type xml
graph = Graph(nodes(donnees), edges(donnees), False, True) # traitement avec la class Graph au dessus

graph_data = graph.make_graph()
noeuds = graph_data.get("nodes") #liste des noeuds
aretes = graph_data.get("vertices") # liste des arêtes
G=nx.Graph() # Gestion des graphes pour l'affichage avec Matplotlib
for noeud in noeuds : G.add_node(noeud)
for (source,destination) in  aretes : G.add_edge(source,destination)
nx.draw(G, with_labels=True, font_weight='bold') # Préparation de l'affichage
plt.show() # affichage

x=nx.floyd_warshall(G) # utilisation de l'algorithme de Floyd-Warshall
tableau=[[x[l][m] for m in noeuds] for l in noeuds]
somme=[sum(ligne) for ligne in tableau] # somme de chaque ligne
dmax=[max(ligne) for ligne in tableau] # distance maximale de chaque ligne
sml={(s,m):[i for ((i,s1),m1) in zip(enumerate(somme),dmax) if s==s1 and m==m1] for ((i,s),m) in zip(enumerate(somme),dmax)}
centre = sml[min(sml)]
rayon=min(sml)[1]
diametre=max(sml)[1]
list_centre = [noeuds[c] if c in centre else "" for c in range(len(somme))]
list_rayon = [rayon if c in centre else "" for c in range(len(somme))]
list_diametre = [diametre if (s,m)==max(sml) else "" for ((i,s),m) in zip(enumerate(somme),dmax)]
df=pandas.DataFrame(tableau, index=noeuds, columns=noeuds)
df["somme"]=somme
df["dist_max"]=dmax
df["centre"]=list_centre
df["rayon"]=list_rayon
df["diametre"]=list_diametre
print(df)
df.to_csv(fichier[:-7]+'csv')
