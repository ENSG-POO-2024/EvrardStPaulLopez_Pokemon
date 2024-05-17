# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:33:02 2024

@author: gaell
"""
import sys
import numpy as np
import pygame
import time
import random
from PyQt5.QtWidgets import QWidget, QLabel,QMainWindow,QApplication,QDialog

from Pokemon import *
from player_turn import *

class Combat(PokemonSauvage, PokemonDresseur) :
    def __init__(self, pokemonJoueur, pokemonSauvage) :
        """
        constructeur de la classe.
        Utile pour instancier l'object
        qui servira à réaliser un combat

        Parameters
        ----------
        pokemonJoueur : TYPE
            DESCRIPTION.
        pokemonSauvage : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.p1 = pokemonJoueur
        self.p2 = pokemonSauvage
        
    def coefficient_attaque(self, p1, p2) :
        """
        Permet de déterminer l'efficacité de l'attaque selon le ou les types 
        de pokemon, et donc de calculer les dégâts infligés selon le type de 
        chacun des pokemons présents dans le combat.
        Parameters
        ----------
        p1 : pokemonJoueur
            DESCRIPTION.
        p2 : PokemonSauvage
            DESCRIPTION.

        Returns
        -------
        coeff : Float
            DESCRIPTION.

        """
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
    
    def calcul_degats(self, p1, p2, type_attaque) :
        """
        Calcul des dégats lorsque l'un des deux pokemons attaque l'autre

        Parameters
        ----------
        p1 : pokemonDresseur
            DESCRIPTION.
        p2 : pokemonSauvage
            DESCRIPTION.
        type_attaque : Str
            DESCRIPTION.

        Returns
        -------
        degats : int
            DESCRIPTION.

        """
        
        defense_adverse = self.p2.defense
        
        if type_attaque == 'Attaque spéciale' :
            attaque = self.p1.attack * self.coefficient_attaque(p1, p2)
        else :
            attaque = self.p1.attack
        
        # Si l'action décidée par le joueur est une attaque neutre, on considère coeff = 1
        degats = np.ceil((attaque * 8) / defense_adverse)
        # Trouvé sur Internet : HPperdus = ceil((((niveau * 4 + 2) * att * coeff) / defense) / 50 + 2)
         
        return degats
    
    def action_joueur(self) :
        """
        Permet au joueur de décider de son action : il peut soit fuir le combat, 
        soit lancer une attaque spéciale, soit lancer une attaque neutre.

        Returns
        -------
        None.

        """
        
        run_app_player_turn()
                    
                
                 
    def action_pokemon_sauvage(self) : 
        """
        Le pokemon adverse a aussi une attaque neutre et une attaque spéciale, 
        il choisit au hasard parmi les deux. 

        Returns
        -------
        None.

        """
        type_attaque = random.random()
        # Si type_attaque > 0.7 attaque spéciale sinon attaque neutre
         
        if type_attaque > 0.7 :
            if self.p1.barreDeVie - self.calcul_degats(self.p2, self.p1, 'Attaque spéciale') >= 0 :
                self.p1.barreDeVie -= self.calcul_degats(self.p2, self.p1, 'Attaque spéciale')
                print(self.p2.nom, " utilise Attaque spéciale et inflige ", self.calcul_degats(self.p1, self.p2, 'Attaque spéciale'), " de dégâts ! ")

            else :
                self.p1.barreDeVie = 0
        else :
            if self.p1.barreDeVie - self.calcul_degats(self.p2, self.p1, 'Attaque neutre') >= 0 :
                self.p1.barreDeVie -= self.calcul_degats(self.p2, self.p1, 'Attaque neutre')
                print(self.p2.nom, " utilise Attaque neutre et inflige ", self.calcul_degats(self.p1, self.p2, 'Attaque neutre'), " de dégâts ! ")

            else :
                self.p1.barreDeVie = 0
        
            
    def attaque_speciale(self) :
        """
        effectue les changements
        liés à une attaque spéciale
        dans les attributs du
        pokemon concerné

        Returns
        -------
        None.

        """
        if (self.p2.barreDeVie - self.calcul_degats(self.p1, self.p2, 'Attaque spéciale')) >= 0 :
            self.p2.barreDeVie -= self.calcul_degats(self.p1, self.p2, 'Attaque spéciale')
            print(self.p1.nom, "utlise Attaque spéciale et inflige ", self.calcul_degats(self.p1, self.p2, 'Attaque spéciale'), " de dégâts ! ")
        else :
            self.p2.barreDeVie = 0

    def attaque_neutre(self) :
        """
        effectue les changements
        liés à une attaque neutre
        dans les attributs du
        pokemon concerné

        Returns
        -------
        None.

        """
        if (self.p2.barreDeVie - self.calcul_degats(self.p1, self.p2, 'Attaque neutre')) >= 0 :
            self.p2.barreDeVie -= self.calcul_degats(self.p1, self.p2, 'Attaque neutre')
            print(self.p1.nom, "utilise Attaque neutre et inflige ", self.calcul_degats(self.p1, self.p2, 'Attaque neutre'), " de dégâts ! ")

        else :
            self.p2.barreDeVie = 0 
         
    def lancement_combat(self) :
        """
        fonction lançant le combat
        renvoye un booléen pour signaler
        à la fenêtre map qu'elle doit
        se figer

        Returns
        -------
        Boolean.

        """
        signal = True
        pygame.init()
        
        fenetre.close()
        
        ost = pygame.mixer.Sound('music/ost_fight.mp3')

        ost.play()
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_player_turn()
        ui.setupUi(dialog, self.p1, self.p2, self)
        ui.ButtonResponse()
        dialog.show()
        
        
        
        sys.exit(app.exec_())
        
        
        return signal

