# Placer des marqueurs sur une carte avec Openstreetmap

Nous allons utiliser la bibliothèque folium de python

Vérifions que la bibliothèque est bien installée avant de commencer puis nous allons ouvrir une carte Openstreetmap avec 2 markeurs et centrer sur le lycée Joliot-Curie

Exécuter la cellule python ci-dessous avec le triangle gris $\rhd$



```python
import os, sys
try :
    import folium
except :
    !pip install folium
finally :
    import folium
print(f"la version de folium est {folium.__version__}\nCelle de python est {sys.version}")

# https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb

"""
colors = [ 'red', 'blue', 'gray', 'darkred', 'lightred', 'orange', 'beige', 'green', 'darkgreen', 'lightgreen', 
'darkblue', 'lightblue', 'purple', 'darkpurple', 'pink', 'cadetblue', 'lightgray', 'black' ] #liste de couleurs
"""
from folium.plugins import MarkerCluster

m = folium.Map(location=[48.126, -1.649], zoom_start=18)
marker_cluster = MarkerCluster().add_to(m)

""" #une fois la location remplie enlever cette ligne
folium.Marker(
    location=[,],# zone Espace Technologique à chercher et remplir 
    popup='STI2D-BTS',
    icon=folium.Icon(color='beige', icon='plug',prefix='fa'), #green, black, white
).add_to(marker_cluster)
""" #une fois la location remplie enlever cette ligne

folium.Marker(
    location=[48.12638,-1.64835],
    popup='CDI',
    icon=folium.Icon(color='purple', icon='book',prefix='fa'), #purple
).add_to(marker_cluster)

""" #une fois la location remplie enlever cette ligne
folium.Marker(
    location=[,], # zone Espace Technologique à chercher et remplir 
    popup='Internat',
    icon=folium.Icon(color='red',icon='hotel', prefix='fa') #red
).add_to(marker_cluster)
""" #une fois la location remplie enlever cette ligne

folium.Marker(
    location=[48.12623, -1.64912],
    popup='SNT',
    icon=folium.Icon(color='blue', icon='laptop',prefix='fa'), #blue
).add_to(marker_cluster)

m.save(os.path.join('Emplacement_Joliot_Curie.html'))
m

```

## Travail à faire !

### Q1) Ajouter 2 markeurs

Ouvrir Openstreetmap https://www.openstreetmap.org 

1. Rechercher "Lycée Joliot Curie, Rennes"
2. Zoomer au maximum
3. Clic droit sur la carte : centrer sur le batiment souhaité
4. Clic droit sur la carte : afficher l'adresse

Repérer dans Openstreetmap  de façon précise la latitude et la longitude de
 + **l'emplacement de l'Espace Technologique** du lycée Joliot-Curie à Rennes
 + **l'emplacement du Batiment G** du lycée Joliot-Curie à Rennes
 
**Remplir les 2 lignes dans le fichier ci-dessus qui se terminent par** *à chercher et remplir*
 
N'oubliez pas d'enlever les 4 lignes qui commencent par """ (3 guillemets) : 

""" #une fois la location remplie enlever cette ligne 

### Exécuter à nouveau la cellule python ci-dessus !

Vous devriez voir 4 markeurs maintenant !

**Attention si rien n'apparaît après des modifications**, il faut relancer le noyau avec <i class="fa-repeat fa"></i> *Restart the kernel*

### Q2) A quoi correspond le popup sur la carte ?
<br><br>

### Q3) Remplacer SNT par SNT-NSI dans le dernier pop-up


# Extra 
Ajoutez d'autres markers pour les batiments D, K et le Restaurant Inter-établissement

Vous pourrez choisir des icones dans  https://github.com/lvoogdt/Leaflet.awesome-markers

### Q4) Sauvegarder votre fichier python_folium_multi_marker_eleves en remplaçant eleves par votre nom et prénom

- Dans cette fenêtre cliquer sur la disquette pour sauvegarder ce fichier.
- Tout en haut à gauche de cette zone, clic droit sur le nom 'python_folium_multi_marker_eleves'  : Rename Notebook : 'python_folium_multi_marker_nom_prenom'
- Dans la fenêtre de gauche clic droit sur le fichier 'python_folium_multi_marker_nom_prenom.ipynb' : Download puis enregistrer le fichier.

### Q5) Sauvegarder le fichier 'Emplacement_Joliot_Curie.html'

- Dans la fenêtre de gauche clic droit sur le fichier 'Emplacement_Joliot_Curie.html' : Download puis enregistrer le fichier.

**Vous devez rendre ces deux fichiers**


```python

```
