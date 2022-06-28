#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:45:53 2019

@author: pierre
"""

# fichier="graph_ajldyXaqChcrtYjG.graphml"
# fichier2="graph_ajldyXaqChcrtYjG1.graphml"
# f=open(fichier2,'w')
# f.write(p)
# f.close()

fichier="graph_ELsSmpuWhtctrRQk.graphml"
f=open(fichier,'r')
texte=f.readline()
l=texte.replace("</edge>","</edge>\n")
m=l.replace("</node>","</node>\n")
o=m.replace("<nodes>","<nodes>\n")
texte=o.replace("<edges>","<edges>\n")
f.close()
noeuds = {}
liaisons=[]
for ligne in texte.split('\n') :
    if "node" in ligne :
        id=ligne.split('id=')[1].split()[0]
        noeud=ligne.split('mainText=')[1].split()[0]
        noeuds[id]=noeud
        print("noeud",id,noeud,noeuds)
    if ("edge") in ligne :
        liaison1=ligne.split("source")[1].split('=')[1].split()[0].strip()
        liaison2=ligne.split("target")[1].split("=")[1].split()[0].strip()
        liaison=(noeuds[liaison1],noeuds[liaison2])
        liaisons.append(liaison)
        print("liaison",liaison1,liaison2,liaison)
print(noeuds,liaisons)


