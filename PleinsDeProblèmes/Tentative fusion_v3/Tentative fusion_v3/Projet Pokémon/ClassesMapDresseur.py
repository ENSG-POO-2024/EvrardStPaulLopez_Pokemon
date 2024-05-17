# -*- coding: utf-8 -*-

import random
from math import sqrt
import csv

from combat_code import *
#from Pokemon import *

with open('pokemon_coordinates.csv',newline='') as coordonnees:
    tableau=[]
    lire=csv.reader(coordonnees) 
    for ligne in lire:
       ligne[1]=eval(ligne[1])
       tableau.append(ligne)  #On obtient le tableau avec le nom du pokémon et ses coordonnées
       
class Map:
    
    def __init__(self,positionDresseur,tableau,DistanceMinimumDecouverte): #Position initiale du dresseur au choix, tableau défini avant, distance à partir de laquelle apparaît le pokémon à l'écran
        self.positionDresseur=positionDresseur
        self.tableau=tableau
        self.DistanceMinimumDecouverte=DistanceMinimumDecouverte
         
    def distance(self, pokemon, positionDresseur): 
        """
        Calcul de la distance entre un pokémon et le dresseur, 
        utile pour afficher le pokémon ou non, pour afficher 
        l'interface de combat ou non

        Parameters
        ----------
        pokemon : pokemonSauvage
            DESCRIPTION.
        positionDresseur : liste à deux éléments
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        
        return sqrt((pokemon[0]-self.positionDresseur[0])**2+(pokemon[1]-self.positionDresseur[1])**2)

class Dresseur:
    
    starter=["Bulbasaur", "Charmander","Squirtle"]
    pokemonDeDepart=[starter[random.randint(0,len(starter)-1)]] #Liste des pokémons que possède le dresseur, le jeu se termine quand elle contient les 151 pokémons, au départ elle contient au hasard un des trois starters
    
    def __init__(self, position, DistanceMinimumDecouverte):
        self.DistanceMinimumDecouverte=DistanceMinimumDecouverte
        self.position=position
        
    # def lanceCombat(self, PokemonAllie, PokemonACapturer):
    #             print("Combat lancé avec un pokémon")
    #             p1 = PokemonAllie #Pouvoir choisir quel pokémon on utilise dans notre liste,ici c'est forcément le starter donc pas fou
    #             p2 = PokemonACapturer
    #             combat= Combat(p1,p2)
    #             # c = combat.coefficient_attaque(p2, p1)
    #             # print(c)
    
    #             # dgts = combat.calcul_degats(p1, p2, 'Attaque spéciale') 
    #             # print(dgts)
    
    #             # print(combat.p2.barreDeVie - combat.calcul_degats(p1, p2, 'Attaque spéciale'))
    
    
    #             combat.lancement_combat()
                

                
