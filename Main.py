###############################
########## Main ###############
###############################

#import de librairies
import numpy as np

#import de classes
from Pokemon import *
from Menu import *

######################################
#####Instanciation des Pokemons ######
######################################

cheminIcone = ""
Salamèche = PokemonSauvage("Salamèche", "Feu", "Eau", 200, cheminIcone)
print(Salamèche)

### AJOUTER CHEMIN ICONE ###

G1 = Pokemons("Génération 1")
print(G1)

Bulbizard = G1["Bulbasaur"]
print(G1)
print("Afficher infos de Bulbizard")
print(Bulbizard)

print("Avant la suppresion de Bulbizard")
print(len(G1))

G1.remove("Bulbasaur")
print(G1)
print("Après la suppresion de Bulbizard")
print(len(G1))
print(G1["Bulbasaur"])

G1.pokemons["Salamèche"] = Salamèche
print(len(G1))
print(G1.pokemons)
###############################################
#########Interface graphique - Menu ###########
###############################################
"""
Jeu = QApplication(sys.argv)
menu = Menu()
sys.exit(Jeu.exec())
"""
