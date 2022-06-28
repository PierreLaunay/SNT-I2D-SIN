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
    x: int
    y: int
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
            id=e.get("id"),
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
#layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit"), sg.Button("Exit")]]
layout = [[sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        window.close()
        break
    elif event == "Submit":
        fichier=values["-IN-"]
        print(values["-IN-"])
        window.close()
        break

with open(fichier, "r") as f: file = f.read()
donnees = bs(file, features="xml")
graph = Graph(nodes(donnees), edges(donnees), False, True)

graph_data = graph.make_graph()
G=nx.Graph()
#print(graph_data)
for noeud in graph_data.get("nodes") : G.add_node(noeud)
for (source,destination) in  graph_data.get("vertices") : G.add_edge(source,destination)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

x=nx.floyd_warshall(G)
tableau=[[x[l][m] for m in graph_data.get("nodes")] for l in graph_data.get("nodes")]
sl=[sum(ligne) for ligne in tableau]
ml=[max(ligne) for ligne in tableau]
sml=[z for z in zip(sl,ml,range(len(sl)))]
centre = min(sml)[-1]
rayon=max(tableau[centre])
diametre=max(sml)[1]
list_centre = [graph_data.get("nodes")[centre] if s==min(sml) else "" for s in sml]
list_rayon = [rayon if s else "" for s in list_centre]
list_diametre = [diametre if s==max(sml) else "" for s in sml]
df=pandas.DataFrame(tableau, index=graph_data.get("nodes"), columns=graph_data.get("nodes"))
df["somme"]=sl
df["dist_max"]=ml
df["centre"]=list_centre
df["rayon"]=list_rayon
df["diametre"]=list_diametre
print(df)
df.to_csv(fichier[:-7]+'csv')