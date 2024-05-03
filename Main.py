###############################
########## Main ###############
###############################

#import de librairies
import numpy as np

#import de classes
from Pokemon import *

################################
#####Instanciation##############
################################

Salamèche = PokemonSauvage("Salamèche", (15, 452), "Feu", 200)
print(Salamèche)

G1 = Pokemons("Génération 1")
print(G1)
Bulbizard = G1['Bulbasaur']
print(Bulbizard)
print("Avant la suppresion de Bulbizard")
print(len(G1))
G1.remove("Bulbasaur")
print("Après la suppresion de Bulbizard")
print(len(G1))
