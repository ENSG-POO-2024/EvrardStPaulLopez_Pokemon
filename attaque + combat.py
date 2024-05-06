# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:33:02 2024

@author: gaell
"""

import numpy as np

class Attaque() :
    def __init__(self, pokemonJoueur, pokemonSauvage) :
        # Pokemons à initialiser ;)
        self.p1 = pokemonJoueur    # On va supposer que l'attaque est du même type que le type 1 du pokemon pour l'instant
        self.p2 = pokemonSauvage
        
    def coefficient_attaque(self) :
        
        # Permet de déterminer l'efficacité de l'attaque selon le ou les types de pokemon, et donc de calculer les dégâts infligés selon le type de chacun des pokemons présents dans le combat.
        
        coeff = 1
        
        if self.p1.type1 == 'Steel' or self.p1.type2 == 'Steel':
            if self.p2.type1 == 'Water' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Steel' or self.p2.type1 == 'Electric' or self.p2.type2 == 'Water' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Electric' :
                coeff *= 0.5
            if self.p2.type1 == 'Ice' or self.p2.type1 == 'Rock' or self.p2.type1 == 'Fairy' or self.p2.type2 == 'Ice' or self.p2.type2 == 'Rock' or self.p2.type2 == 'Fairy' :
                coeff *= 2
        
        if self.p1.type1 == 'Fighting' or self.p1.type2 == 'Fighting' :
            if self.p2.type1 == 'Bug' or self.p2.type1 == 'Poison' or self.p2.type1 == 'Psychic' or self.p2.type1 == 'Flying' or self.p2.type1 == 'Fairy' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Poison' or self.p2.type2 == 'Psychic' or self.p2.type2 == 'Flying' or self.p2.type2 == 'Fairy' :
                coeff *= 0.5
            if self.p2.type1 == 'Ghost' or self.p2.type2 == 'Ghost' :
                coeff *= 0
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Ice' or self.p2.type1 == 'Normal' or self.p2.type1 == 'Rock' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Ice' or self.p2.type2 == 'Normal' or self.p2.type2 == 'Rock' :
                coeff *= 2
        
        if self.p1.type1 == 'Dragon' or self.p1.type2 == 'Dragon' :
            if self.p2.type1 == 'Steel' or self.p2.type2 == 'Steel' :
                coeff *= 0.5
            if self.p2.type1 == 'Dragon' or self.p2.type2 == 'Dragon' :
                coeff *= 2
            if self.p2.type1 == 'Fairy' or self.p2.type2 == 'Fairy' :
                coeff *= 0
        
        if self.p1.type1 == 'Water' or self.p1.type2 == 'Water':
            if self.p2.type1 == 'Dragon' or self.p2.type1 == 'Water' or self.p2.type1 == 'Grass' or self.p2.type2 == 'Dragon' or self.p2.type2 == 'Water' or self.p2.type2 == 'Grass' :
                coeff *= 0.5
            if self.p2.type1 == 'Fire' or self.p2.type1 == 'Rock' or self.p2.type1 == 'Ground' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Rock' or self.p2.type2 == 'Ground' :
                coeff *= 2
        
        if self.p1.type1 == 'Electric' or self.p1.type2 == 'Electric' :
            if self.p2.type1 == 'Dragon' or self.p2.type1 == 'Electric' or self.p2.type1 ==  'Grass' or self.p2.type2 == 'Dragon' or self.p2.type2 == 'Electric' or self.p2.type2 ==  'Grass' :
                coeff *= 0.5
            if self.p2.type1 == 'Water' or self.p2.type1 == 'Flying' or self.p2.type2 == 'Water' or self.p2.type2 == 'Flying' :
                coeff *= 2
            if self.p2.type1 == 'Ground' or self.p2.type2 == 'Ground' :
                coeff *= 0
            
        if self.p1.type1 == 'Fire' or self.p1.type2 == 'Fire' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Ice' or self.p2.type1 == 'Bug' or self.p2.type1 == 'Grass' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Ice' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Grass' :
                coeff *= 2
            if self.p2.type1 == 'Dragon' or self.p2.type1 == 'Water' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Rock' or self.p2.type2 == 'Dragon' or self.p2.type2 == 'Water' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Rock' :
                coeff *= 0.5
        
        if self.p1.type1 == 'Fairy' or self.p1.type2 == 'Fairy' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Poison' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Poison' :
                coeff *= 0.5
            if self.p2.type1 == 'Fighting' or self.p2.type1 == 'Dragon' or self.p2.type2 == 'Fighting' or self.p2.type2 == 'Dragon' :
                coeff *= 2
            
        if self.p1.type1 == 'Ice' or self.p1.type2 == 'Ice' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Water' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Ice' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Water' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Ice' :
                coeff *= 0.5
            if self.p2.type1 == 'Dragon' or self.p2.type1 == 'Grass' or self.p2.type1 == 'Ground' or self.p2.type1 == 'Flying' or self.p2.type2 == 'Dragon' or self.p2.type2 == 'Grass' or self.p2.type2 == 'Ground' or self.p2.type2 == 'Flying' :
                coeff *= 2
                
        if self.p1.type1 == 'Bug' or self.p1.type2 == 'Bug' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Fighting' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Poison' or self.p2.type1 == 'Ghost' or self.p2.type1 == 'Flying' or self.p2.type1 == 'Fairy' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Fighting' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Poison' or self.p2.type2 == 'Ghost' or self.p2.type2 == 'Flying' or self.p2.type2 == 'Fairy' :
                coeff *= 0.5
            if self.p2.type1 == 'Grass' or self.p2.type1 == 'Psychic' or self.p2.type2 == 'Grass' or self.p2.type2 == 'Psychic' :
                coeff *= 2
        
        if self.p1.type1 == 'Normal' or self.p1.type2 == 'Normal' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Rock' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Rock' :
                coeff *= 0.5
            if self.p2.type1 == 'Ghost' or self.p2.type2 == 'Ghost' :
                coeff *= 0
        
        if self.p1.type1 == 'Grass' or self.p1.type2 == 'Grass' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Dragon' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Bug' or self.p2.type1 == 'Grass' or self.p2.type1 == 'Poison' or self.p2.type1 == 'Flying' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Dragon' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Grass' or self.p2.type2 == 'Poison' or self.p2.type2 == 'Flying' :
                coeff *= 0.5
            if self.p2.type1 == 'Water' or self.p2.type1 == 'Rock' or self.p2.type1 == 'Ground' or self.p2.type2 == 'Water' or self.p2.type2 == 'Rock' or self.p2.type2 == 'Ground' :
                coeff *= 2
        
        if self.p1.type1 == 'Poison' or self.p1.type2 == 'Poison' :
            if self.p2.type1 == 'Steel' or self.p2.type2 == 'Steel' : 
                coeff *= 0
            if self.p2.type1 == 'Grass' or self.p2.type1 == 'Fairy' or self.p2.type2 == 'Grass' or self.p2.type2 == 'Fairy' :
                coeff *= 2
            if self.p2.type1 == 'Poison' or self.p2.type1 == 'Rock' or self.p2.type1 == 'Soil' or self.p2.type1 == 'Ghost' or self.p2.type2 == 'Poison' or self.p2.type2 == 'Rock' or self.p2.type2 == 'Soil' or self.p2.type2 == 'Ghost' :
                coeff *= 0.5
            
        if self.p1.type1 == 'Psychic' or self.p1.type2 == 'Psychic' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Psychic' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Psychic' :
                coeff *= 0.5
            if self.p2.type1 == 'Fighting' or self.p2.type1 == 'Poison' or self.p2.type2 == 'Fighting' or self.p2.type2 == 'Poison' :
                coeff *= 2
            
        if self.p1.type1 == 'Rock' or self.p1.type2 == 'Rock' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Fighting' or self.p2.type1 == 'Ground' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Fighting' or self.p2.type2 == 'Ground' :
                coeff *= 0.5
            if self.p2.type1 == 'Fire' or self.p2.type1 == 'Ice' or self.p2.type1 == 'Bug' or self.p2.type1 == 'Flying' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Ice' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Flying' :
                coeff *= 2
            
        if self.p1.type1 == 'Ground' or self.p1.type2 == 'Ground' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Fire' or self.p2.type1 == 'Electric' or self.p2.type1 == 'Poison' or self.p2.type1 == 'Rock' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Fire' or self.p2.type2 == 'Electric' or self.p2.type2 == 'Poison' or self.p2.type2 == 'Rock' :
                coeff *= 2
            if self.p2.type1 == 'Bug' or self.p2.type1 == 'Grass' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Grass' :
                coeff *= 0.5
            
        if self.p1.type1 == 'Ghost' or self.p1.type2 == 'Ghost' :
            if self.p2.type1 == 'Normal' or self.p2.type2 == 'Normal' :
                coeff *= 0
            if self.p2.type1 == 'Psychic' or self.p2.type1 == 'Ghost' or self.p2.type2 == 'Psychic' or self.p2.type2 == 'Ghost' :
                coeff *= 2
            
        if self.p1.type1 == 'Flying' or self.p1.type2 == 'Flying' :
            if self.p2.type1 == 'Steel' or self.p2.type1 == 'Electric' or self.p2.type1 == 'Rock' or self.p2.type2 == 'Steel' or self.p2.type2 == 'Electric' or self.p2.type2 == 'Rock' :
                coeff *= 0.5
            if self.p2.type1 == 'Fighting' or self.p2.type1 == 'Bug' or self.p2.type1 == 'Grass' or self.p2.type2 == 'Fighting' or self.p2.type2 == 'Bug' or self.p2.type2 == 'Grass' :
                coeff *= 2
            
        return coeff
    
    def calcul_degats(self, type_attaque) :
        # Il faudra définir quel pokemon attaque en premier, mais là je suppose que p1 attaque p2
        
        defense_adverse = self.p2.defense
        
        if type_attaque == 'Attaque spéciale' :
            attaque = self.p1.attack * self.coefficient_attaque()
        else :
            attaque = self.p1.attack
        
        # Si l'action décidée par le joueur est une attaque neutre, on considère coeff = 1
        degats = np.ceil((((0.4 + 2) * attaque * 100) / defense_adverse) / 50 + 2)
        # Trouvé sur Internet : HPperdus = ceil((((niveau * 4 + 2) * att * coeff) / defense) / 50 + 2)
        
        return degats
    
    def action_joueur(self) :
        # Permet au joueur de décider de son action : il peut soit fuir le combat, soit lancer une attaque spéciale, soit lancer une attaque neutre.
        action = input('Attaque neutre, Attaque spéciale, Fuite ?')
        
        if action == 'Fuite' :
            pass
        elif action == 'Attaque spéciale' :
            self.p2.hp -= self.calcul_degats('Attaque spéciale')
        else :
            self.p2.hp -= self.calcul_degats('Attaque neutre')
        
        

if __name__ == "__main__" :
    dgts = (((0.4 + 2) * 49 * 100) / 63) / 50 + 2
    print(dgts)