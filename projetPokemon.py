import random
import math
class dresseur:
    starter=["Bulbizarre", "Salamèche","Carapuce"]
    pokemonDeDepart=starter[random.randint(0,len(starter)-1)]
    DistanceMinimumDecouverte=2
    def __init__(self,position,dx,dy):
        self.position=position
        self.dx=dx
        self.dy=dy
    def miseAjourPosition(self):
        self.position.translate(self.dx, self.dy)
    def DecouvertePokemonSauvage(self,CoordPokemon):
        if sqrt((CoordPokemon[0]-self.position[0])**2+(CoordPokemon[1]-self.position[2])**2)<DistanceMinimumDecouverte:
            #Le pokémon apparaît
        if CoordPokemon[0]-self.position[0])**2+(CoordPokemon[1]-self.position[2])**2==0:
            #Le combat se lance
    #Si le combat gagné, ajouter le pokemonSauvage au starter
    # def eviteMur(self):
        
    #     # Les coordonnées des bords de map
    #     xmin = 0
    #     xmax = 40
    #     ymin = 0
    #     ymax = 40
        
    #     # Etape 1: on s'arrête au bord
    #     if self.position.x < xmin:
    #         self.position.x = xmin
    #     if self.position.x > xmax:
    #         self.position.x = xmax
    #     if self.position.y < ymin:
    #         self.position.y = ymin
    #     if self.position.y > ymax:
    #         self.position.y = ymax
        
    #     # Etape 2: Change de direction
    #     if (self.position.x - xmin) < dresseur.distance_min:
    #         self.dx += dresseur.turnFactor
    #         self.normaliserVitesse()
    #         return True
    #     elif (xmax - self.position.x) < Poisson.distance_min:
    #         self.dx -= Poisson.turnFactor
    #         self.normaliserVitesse()
    #         return True
    #     elif (self.position.y - ymin) < Poisson.distance_min:
    #         self.dy += Poisson.turnFactor
    #         self.normaliserVitesse()
    #         return True
    #     elif (ymax - self.position.y) < Poisson.distance_min:
    #         self.dy -= Poisson.turnFactor
    #         self.normaliserVitesse()
    #         return True

    #     return False        
