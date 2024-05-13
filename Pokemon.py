import numpy as np
import random as rd
import pandas as pd
import os

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
    def __init__(self, nom, Coord, type1, type2, barreDeVie):
        self.Coord = Coord
        self.type1 = type1
        self.type2 = type2
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
        txt += ". Je suis de type1 " + str(self.type1)
        txt += " et de type2 " + str(self.type2)
        txt += ". Je rôde en " + str(self.Coord)
        txt += ". J'ai " + str(self.barreDeVie) + " points de vie restants"
        
        return txt
    
    def __repr__(self):
        txt = "Je m'appelle "
        txt += str(self.nom)
        txt += ". Je suis de type1 " + str(self.type1)
        txt += " et de type2 " + str(self.type2)
        txt += ". Je rôde en " + str(self.Coord)
        txt += ". J'ai " + str(self.barreDeVie) + " points de vie restants"
        return txt
    
class PokemonDresseur(Pokemon):
    def __init__(self, nom, type1, type2, barreDeVie, icone):
        self.nom = nom
        self.type1 = type1
        self.type2 = type2
        self.barreDeVie = barreDeVie
        #un objet Pokemon contient son icône
        #pour son affichage
        self.icone = icone

    def attaquer(self, pokemonAttaque):
        return
    def mourir(self):
        return
    def supprimer(self):
        return
    
    def __str__(self):
        txt = "Je m'appelle "
        txt += str(self.nom)
        txt += ". Je suis un " + str(self.nom)
        txt += ". Je suis de type " + str(self.type)
        #un pokemon domestique n'a pas de position
        #il est dans le deck du dresseur
        txt += ". J'ai " + str(self.barreDeVie) + " points de vie restant"
        return txt

class Pokemons(PokemonSauvage):
    def __init__(self, nom):
        self.nom = nom
        tableau_pokemon = pd.read_csv('data/pokemon_first_gen.csv')
        #on crée l'objet Pokemon dans une colonne du tableau
        self.pokemons = {}
        nomPokemon = tableau_pokemon['Name'].tolist()
        for i in range(0, 151):
            nom = tableau_pokemon['Name'][i]
            type1 = tableau_pokemon['Type 1'][i]
            type2 = tableau_pokemon['Type 2'][i]
            hp = tableau_pokemon['HP'][i]
            #erreur quand j'utilise random pour génèrer les coordonnées: affiche le pointeur, pas le résultat;
            Coord = (10, 349)

            self.pokemons[nomPokemon[i]] = PokemonSauvage(nom, Coord, type1, type2, hp)

    def __len__(self):
        """
        obtenir le nombre de pokemons sauvages présents dans l'objet
        """
        return len(self.pokemons)
    
    def __str__(self):
        """
        afficher les informations utiles du groupe de Pokemons
        """
        txt = "Nous sommes les Pokemons de la "
        txt += self.nom
        #txt += ". Et nous sommes " + len(self.pokemons)
        return txt
    def __repr__(self):
        """
        afficher les informations utiles du groupe de Pokemons
        """
        txt = "Nous sommes les Pokemons de la "
        txt += self.nom
        #txt += ". Et nous sommes " + len(self.pokemons)
        return txt
    
    def remove(self, nomPokemon):
        """
        Supprimer un Pokemon sauvage lorsqu'il est capturé
        """
        if isinstance(nomPokemon, str):
            self.pokemons.pop(nomPokemon)
            #del self.pokemons[nomPokemon]
        else:
            print(str(nomPokemon.nom) + " n'est pas un pokemon.")
    
    def __getitem__(self, clePokemon):
        """
        récupèrer un Pokemon à partir de son nom (puisque chaque instance est unique)
        renvoyer diff selon type de l'entrée entre crochet
        si coord renvoyer ça, si str renvoyer ça, si type renvoyer types, 
        """
        if isinstance(clePokemon, str):
            #appel via dictionnaire
            if clePokemon in self.pokemons:
                return self.pokemons[clePokemon]
            else:
                print (str(clePokemon) + " n'est pas dans le tableau")
        else:
            print(str(clePokemon) +" n'est pas un pokemon.")

   #pour ajouter un pokemon
   #pas de surcharge de __add__() pour les dictionnaires

   