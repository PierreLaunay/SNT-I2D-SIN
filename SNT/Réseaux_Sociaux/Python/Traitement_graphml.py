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
# G=nx.Graph()

# fichier="graph_ELsSmpuWhtctrRQk.graphml"
# with open(fichier, "r") as f: file = f.read()

# donnees = bs(file, features="lxml")

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
            maintext=n.get("maintext"),
            x=float(n.get("positionx")),
            y=float(n.get("positiony")),
            size=int(n.get("size")),
            uptext=n.get("uptext"),
        )
        for n in data.select("node")
    ]
    return Nodes
def edges(data) :
    Edges = [
        Edge(
            id=e.get("id"),
            model_value=float(e.get("model_curvedvalue")),
            model_type=int(e.get("model_type")),
            model_width=int(e.get("model_width")),
            isdirect=bool(e.get("isdirect")),
            source=int(e.get("source")),
            target=int(e.get("target")),
            text=e.get("text"),
            uptext=e.get("uptext"),
            weight=int(e.get("weight")),
        )
        for e in donnees.select("edge")
    ]
    return Edges

###########################################



#fichier="Cours_exemple_3/graph_exemple3.graphml"
with open(fichier, "r") as f: file = f.read()

donnees = bs(file, features="lxml")
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
centre=sl.index(min(sl))
rayon=max(tableau[centre])
diametre=max(tableau[sl.index(max(sl))])
list_centre = [graph_data.get("nodes")[centre] if s==min(sl) else "" for s in sl]
list_rayon = [rayon if s else "" for s in list_centre]
list_diametre = [diametre if s==max(sl) else "" for s in sl]
#print("centre",centre,", rayon",rayon,", diamètre",diametre)
df=pandas.DataFrame(tableau, index=graph_data.get("nodes"), columns=graph_data.get("nodes"))
df["somme"]=sl
df["centre"]=list_centre
df["rayon"]=list_rayon
df["diametre"]=list_diametre
print(df)
