# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:33:02 2024

@author: gaell
"""

import numpy as np
import time
import random 
from Pokemon import *
from battle_starts import *
from player_turn import *
from a_pokemon_has_appeared import *
from ennemy_turn import *
from player_loses import *
from player_wins import *

class Attaque(PokemonSauvage, PokemonDresseur) :
    def __init__(self, pokemonJoueur, pokemonSauvage) :
        self.p1 = pokemonJoueur
        self.p2 = pokemonSauvage
        
    def coefficient_attaque(self, p1, p2) :
        
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
    
    def calcul_degats(self, p1, p2, type_attaque) :
        
        # Calcul des dégats lorsque l'un des deux pokemons attaque l'autre
        
        defense_adverse = self.p2.defense
        
        if type_attaque == 'Attaque spéciale' :
            attaque = self.p1.attack * self.coefficient_attaque(p1, p2)
        else :
            attaque = self.p1.attack
        
        # Si l'action décidée par le joueur est une attaque neutre, on considère coeff = 1
        degats = np.ceil((((0.4 + 2) * attaque * 100) / defense_adverse) / 50 + 2)
        # Trouvé sur Internet : HPperdus = ceil((((niveau * 4 + 2) * att * coeff) / defense) / 50 + 2)
         
        return degats
    
    def action_joueur(self) :
        
        #print("C'est votre tour !")
        # Permet au joueur de décider de son action : il peut soit fuir le combat, soit lancer une attaque spéciale, soit lancer une attaque neutre.
        
        run_app_player_turn()
        
        #run_app_battle_starts() # Pour montrer les PV de l'ennemi après l'attaque
            
                
                
    def action_pokemon_sauvage(self) : 
        
        
        #print("C'est le tour de l'adversaire !")
        # Le pokemon adverse a aussi une attaque neutre et une attaque spéciale, il choisit au hasard parmi les deux.
        
        type_attaque = random.random()
        # Si type_attaque > 0.7 attaque spéciale sinon attaque neutre
         
        if type_attaque > 0.7 :
            if self.p1.barreDeVie - self.calcul_degats(p2, p1, 'Attaque spéciale') >= 0 :
                self.p1.barreDeVie -= self.calcul_degats(p2, p1, 'Attaque spéciale')
                print(p2.nom, " utilise Attaque spéciale et inflige ", combat.calcul_degats(p1, p2, 'Attaque spéciale'), " de dégâts ! ")

            else :
                self.p1.barreDeVie = 0
        else :
            if self.p1.barreDeVie - self.calcul_degats(p2, p1, 'Attaque neutre') >= 0 :
                self.p1.barreDeVie -= self.calcul_degats(p2, p1, 'Attaque neutre')
                print(p2.nom, " utilise Attaque neutre et inflige ", combat.calcul_degats(p1, p2, 'Attaque neutre'), " de dégâts ! ")

            else :
                self.p1.barreDeVie = 0
            
 
    def test_victoire(self) :
        if self.p1.barreDeVie > 0 and self.p2.barreDeVie == 0 :
             return 'Victoire' # True si le joueur gagne, False sinon
        elif self.p1.barreDeVie == 0 and self.p2.barreDeVie > 0 :
            return 'Défaite'
            
    def attaque_speciale(self) :
        if (combat.p2.barreDeVie - combat.calcul_degats(p1, p2, 'Attaque spéciale')) >= 0 :
            combat.p2.barreDeVie -= combat.calcul_degats(p1, p2, 'Attaque spéciale')
            print(p1.nom, "utlise Attaque spéciale et inflige ", combat.calcul_degats(p1, p2, 'Attaque spéciale'), " de dégâts ! ")
        else :
            combat.p2.barreDeVie = 0

    def attaque_neutre(self) :
        if (combat.p2.barreDeVie - combat.calcul_degats(p1, p2, 'Attaque neutre')) >= 0 :
            combat.p2.barreDeVie -= combat.calcul_degats(p1, p2, 'Attaque neutre')
            print(p1.nom, "utilise Attaque neutre et inflige ", combat.calcul_degats(p1, p2, 'Attaque neutre'), " de dégâts ! ")

        else :
            combat.p2.barreDeVie = 0
            
    def lancement_combat(self) :
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_player_turn()
        ui.setupUi(dialog, p1, p2)        
        dialog.show()
        ui.ButtonResponse(combat)
        
        
        sys.exit(app.exec_())
        
        
                 

if __name__=="__main__":
    
    p1 = PokemonDresseur('Wartortle', 'Water', 'Psychic', 59, 80, 63)
    p2 = PokemonSauvage('Beedrill', [2.54, 8.36], 'Bug', 'Poison', 65, 90, 47)
    
    combat = Attaque(p1, p2)
     
    #c = combat.coefficient_attaque()
    
    dgts = combat.calcul_degats(p1, p2, 'Attaque spéciale') 
    print(dgts)
    
    print(combat.p2.barreDeVie - combat.calcul_degats(p1, p2, 'Attaque spéciale'))
    
    
    
    def run_app_battle_starts():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_battle_starts()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        QtCore.QTimer.singleShot(20000, dialog.close)
        sys.exit(app.exec_())
        
    #run_app_battle_starts() 
    
    def run_app_player_turn():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_player_turn()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        ui.ButtonResponse(combat)
        sys.exit(app.exec_())
    
    #run_app_player_turn()


    def run_app_pokemon_appeared():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_pokemon_appeared()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        sys.exit(app.exec_()) 
    
    #run_app_pokemon_appeared()
    
    def run_app_ennemy_turn():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_ennemy_turn()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        sys.exit(app.exec_())
        
    #run_app_ennemy_turn()
    
    def run_app_player_loses():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_player_loses()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        sys.exit(app.exec_())
        
    #run_app_player_loses()
    
    
    def run_app_player_wins():
        
        app = QApplication(sys.argv)
        dialog = QDialog()
        ui = Ui_Dialog_player_wins()
        ui.setupUi(dialog, p1, p2)
        dialog.show()
        sys.exit(app.exec_())
        
    #run_app_player_wins()
    
    combat.lancement_combat()