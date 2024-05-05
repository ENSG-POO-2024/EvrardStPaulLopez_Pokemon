import random
from math import sqrt
import matplotlib.pyplot as plt
import csv
with open('pokemon_coordinates.csv',newline='') as coordonnees:
    tableau=[]
    lire=csv.reader(coordonnees) 
    for ligne in lire:
       ligne[1]=eval(ligne[1]) #retirer les pokemons pas de 1ere génération pour le code combat, obligatoire pour gaelle
       tableau.append(ligne)
class Map:
    def __init__(self,positionDresseur,tableau,DistanceMinimumDecouverte):
        self.positionDresseur=positionDresseur
        self.tableau=tableau
        self.DistanceMinimumDecouverte=DistanceMinimumDecouverte
    def grille(self):
        abscisses=[]
        ordonnées=[]
        for i in range(len(tableau)):
            if sqrt((tableau[i][1][0]-self.positionDresseur[0])**2+(tableau[i][1][1]-self.positionDresseur[1])**2)>self.DistanceMinimumDecouverte:
                
              abscisses.append((tableau[i][1][0]))
              ordonnées.append((tableau[i][1][1])) #Il faut que le point en question représente le pokémon à cette position et ses caractéristiques, car utilisé pour le combat ensuite
        plt.figure()
        fig, ax = plt.subplots(figsize=(12, 6)) #taille de la fenêtre
        plt.xlim(0,40)
        plt.ylim(0,10)
        plt.plot(self.positionDresseur[0],self.positionDresseur[1],'x',label="dresseur")
        plt.plot(abscisses,ordonnées,'o',markersize=3,label="Pokémons à découvrir")
        for i in range(len(tableau)):
            if sqrt((tableau[i][1][0]-self.positionDresseur[0])**2+(tableau[i][1][1]-self.positionDresseur[1])**2)<self.DistanceMinimumDecouverte:
                   ax.text(tableau[i][1][0], tableau[i][1][1], tableau[i][0], fontsize=8) #comme le plt.text mais avec choix de la taille de police
        plt.legend(loc='upper left', bbox_to_anchor=(0, 1)) #fixer la légende dans le coin supérieur gauche
        plt.show()
class Dresseur:
    starter=["Bulbizarre", "Salamèche","Carapuce"]
    pokemonDeDepart=[starter[random.randint(0,len(starter)-1)]]
    def __init__(self,position,dx,dy):
        self.position=position
        self.dx=dx
        self.dy=dy
    def translate(self):  
        self.position[0] += self.dx
        self.position[1] += self.dy
        return self.position

    def lanceCombat(self, tableau):
        for pokemon in tableau:
            if self.position == pokemon[1]:  # Vérifie si la position du dresseur correspond à celle d'un Pokémon
                print(f"Combat lancé avec {pokemon[0]}")
                #Code de combat, voir avec Gaelle, possibilité de fuir à implémenter
                #Si le combat est gagné:
                if pokemon[0] not in self.pokemonDeDepart:
                    self.pokemonDeDepart.append(pokemon[0])

    def eviteMur(self):
        if self.position[0] > 40 or self.position[0] < 0:
            self.position[0] -= self.dx  
        if self.position[1] > 10 or self.position[1] < 0:
            self.position[1] -= self.dy 
            
if __name__ == '__main__':
    dresseur=Dresseur([0,0],31.445398005630054, 5.634905916753981)
    position_dresseur=dresseur.translate()
    remiseEnMap=dresseur.eviteMur()
    Carte=Map(position_dresseur, tableau,2)
    combat=dresseur.lanceCombat(tableau)
    Carte.grille()


#J'ai bien la map, les points qui s'enlèvent quand les noms les remplacent en fonction du rayon choisi(dresseur à proximité), et le dresseur se déplace, et ne peut pas sortir de la map,n'importe quelle position de départ possible, utile pour deplacement en temps réel
#Problèmes : la sortie de map considère que les déplacements sont de 1 maximum, si je suis en 0,0 et que je me déplace de -2, je serais pas remis sur la map : résolu
#2eme problème: si mes déplacements ne sont que entiers, je ne pourrais pas me superposer à un pokémon pour lancer un combat:problème résolu, evitemur peut prendre décimaux
#Tester avec Machoke, si on est dessus combat se lance et est bien rajouter à la liste Dresseur.pokemonDeDepart si combat gagné
