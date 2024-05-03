import random
from math import sqrt
import matplotlib.pyplot as plt
import csv
import numpy as np
with open('pokemon_coordinates.csv',newline='') as coordonnees:
    tableau=[]
    lire=csv.reader(coordonnees) 
    for ligne in lire:
       ligne[1]=eval(ligne[1]) #tej les pokemons pas de 1ere génération pour le code combat
       tableau.append(ligne)
class Map:
    def __init__(self,positionDresseur,tableau):
        self.positionDresseur=(0,0)
        self.tableau=tableau
    def grille(self):
        abscisses=[]
        ordonnées=[]
        for i in range(len(tableau)):
            
            abscisses.append((tableau[i][1][0]))
            ordonnées.append((tableau[i][1][1])) #Il faut que le point en question représente le pokémon à cette position et ses caractéristiques
        plt.figure()
        plt.plot(self.positionDresseur[0],self.positionDresseur[1],'x')
        plt.plot(abscisses,ordonnées,'o')
        plt.show()
class Dresseur:
    starter=["Bulbizarre", "Salamèche","Carapuce"]
    pokemonDeDepart=starter[random.randint(0,len(starter)-1)]
    DistanceMinimumDecouverte=2
    tailleMap=40
    def __init__(self,position,dx,dy):
        self.position=position
        self.dx=dx
        self.dy=dy
    def translate(self, dx, dy):  
        self.x += dx
        self.y += dy
    def DecouvertePokemonSauvage(self,CoordPokemon,indice):
        if sqrt((CoordPokemon[0]-self.position[0])**2+(CoordPokemon[1]-self.position[1])**2)<self.DistanceMinimumDecouverte:
            
                    plt.text(CoordPokemon[0],CoordPokemon[1],tableau[indice][0])
                    #On change le point (invisible) par son nom quand on est assez proche
        return Map(self.position, tableau)
        # if (CoordPokemon[0]-self.position[0])**2+(CoordPokemon[1]-self.position[2])**2==0:
            #Le combat se lance
    #Si le combat gagné, ajouter le pokemonSauvage au starter
    def eviteMur(self):
        if self.dx+1>=40:
            self.dx-=1
        if self.dx-1<=0 :
            self.dx+=1
        if self.dy+1>=40:
            self.dy-=1
        if self.dy-1<=0:
            self.dy+=1
            
if __name__ == '__main__':
    positionDresseur=(0,0)
    Carte=Map(positionDresseur, tableau)
   # Carte.grille()
    Dresseur=Dresseur(positionDresseur, 0,0)
    Dresseur.DecouvertePokemonSauvage([0.05310017714857729, 0.7435076839591537],863).grille() #Test de changer un point en son pokémon


#joueur d'un point sur la carte, class map pour définir la grille et les coord des pokémons ainsi que celles de départ du dresseur,compléter le pokemon appaaît
