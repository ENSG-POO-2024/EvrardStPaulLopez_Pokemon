import numpy as np
import random as rd
import pandas as pd

from abc import abstractmethod
class Pokemon:
    def __init__(self):
        type = type #le type du Pokemon
        barreDeVie = barreDeVie #son nombre de points de vie
        nom = nom
    @abstractmethod
    def attaquer():
        return
    def mourir():
        return
    def supprimer():
        return

class PokemonSauvage(Pokemon):
    def __init__(self, nom, position, type, barreDeVie):
        self.position = position
        self.type = type
        #il y aura 151 pokemons distincts donc
        #le nom peut-être la clé primaire
        #pour identifier l'instance Pokemon sauvage
        #au cours du jeu
        self.nom = nom
        self.barreDeVie = barreDeVie
    def attaquer(self, pokemonAttaque):
        """
        gèrer l'attaque faite par le pokemon
        """
        #faire appel à la classe attaque pour gèrer l'attaque
        return
    def supprimer(self):
        #lorsque le pokemon est capturé
        #l'instance de Pokemon sauvage 
        #qu'il représentait disparaît
        del self
        return
    def mourir(self):
        if self.barreDeVie < 5:
            #lorsque le pokemon est capturé
            #on crée son équivalent en pokemon du dresseur
            self.nom = PokemonDresseur(self.nom, self.type, self.barreDeVie)
            self.supprimer()
        return
    def __str__(self):
        txt = "Je m'appelle "
        txt += str(self.nom)
        txt += ". Je suis de type " + str(self.type)
        txt += ". Je rôde en " + str(self.position)
        txt += ". J'ai " + str(self.barreDeVie) + " points de vie restants"
        return txt
    
class PokemonDresseur(Pokemon):
    def __init__(self, nom, type, barreDeVie):
        self.nom = nom
        self.type = TypeError
        self.barreDeVie = barreDeVie

    def attaquer(self, pokemonAttaque):
        return
    def mourir(self):
        return
    def supprimer(self):
        return
    
    def __str__(self):
        txt = "Je m'appelle "
        txt += str(self.nom)
        txt += ". Je suis un " + clasq
        txt += ". Je suis de type " + str(self.type)
        #un pokemon domestique n'a pas de position
        #il est dans le deck du dresseur
        txt += ". J'ai " + str(self.barreDeVie) + " points de vie restants"
        return txt

class Pokemons(PokemonSauvage):
    def __init__(self, nom):
        self.nom = "Generation 1"
        self.Pokemons = []
        tableau_pokemon = pd.read_csv("./EvrardStPaulLopez_Pokemon/data/pokemon_first_gen.csv")
        #on crée l'objet Pokemon dans une colonne du tableau
        tableau_pokemon['Pokemon'] = PokemonSauvage(tableau_pokemon['Name'], (rd.random, rd.random), tableau_pokemon['Type 1'], tableau_pokemon['HP'])
        #à ce stade, la position est aléatoire
        self.Pokemons = tableau_pokemon['Pokemon'].tolist()
        
    def __len__(self):
        """
        obtenir le nombre de pokemons sauvages présents dans l'objet
        """
        return len(self.Pokemons)
    def __str__(self):
        """
        afficher les informations utiles du groupe de Pokemons
        """
        txt = "Nous sommes les Pokemons de la "
        txt += self.nom
        return txt
    def remove(self, nomPokemon):
        """
        Supprimer un Pokemon sauvage lorsqu'il est capturé
        """
        if isinstance(nomPokemon, Pokemon):
            del self.Pokemons.pop(nomPokemon)
        return
    
    def __getitem__(self, nomPokemon):
        """
        récupèrer un Pokemon à partir de son nom (puisque chaque instance est unique)
        """
        if isinstance(nomPokemon, Pokemon):
            return self.Pokemons[nomPokemon]