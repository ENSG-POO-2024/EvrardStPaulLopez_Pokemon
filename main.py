
# -*- coding: utf-8 -*-

import pygame
import os
import time as t

from ClassesMapDresseur import *

# Initialisation du module permettant le jeu
pygame.init()

#musique de fond
musique = pygame.mixer.Sound('musique_map.mp3')
musique.play()


# Définition de la taille de la fenêtre pour qu'elle corresponde à la taille de la carte
largeur = 1100
hauteur = 570
fenetre = pygame.display.set_mode((largeur, hauteur))

#Nom de la fenêtre
pygame.display.set_caption("Pokémon")

#Couleur utilisée pour le fond de la fenêtre
Blanc = (255, 255, 255)

Taille_dresseur=(40,40)

# Chargement des images
#Images du dresseur dans les 4 positions possibles, dont la taille est ajustée pour eviter qu'il soit trop gros
dresseur_gauche = pygame.transform.scale(pygame.image.load('dresseur_gauche.png'), Taille_dresseur)
dresseur_droite = pygame.transform.scale(pygame.image.load('dresseur_droite.png'), Taille_dresseur)
dresseur_face = pygame.transform.scale(pygame.image.load('dresseur_face.png'), Taille_dresseur)
dresseur_dos = pygame.transform.scale(pygame.image.load('dresseur_dos.png'), Taille_dresseur) 
#Image de la map 
carte= pygame.image.load('map.jpg')

# Chemin du dossier avec les images des pokémons, car les images ne sont 
#pas au même niveau que le script, chemin à adapter quand le code est ouvert 
#sur un autre PC
images_pokemons = os.path.join(os.path.dirname(__file__), './Pokemons_pic')

boutons_combat = [] #Liste qui permettra d'avoir un bouton de lancement de combat par pokémon
pokemon_img = [] #liste contenant les images des pokémons et leurs coordonnées associés, créee à partir de ClassesMapDresseur.tableau qui contient les noms au lieu des images

Taille_Pokemon = (50,50) #on met tous les pokémons à la même taille, et suffisamment petits pour qu'ils rentrent tous
Taille_Bouton = (50,50) #La même image de bouton est utilisée pour chaque pokémon, mais on réduit quand même sa taille par soucis de place

for w in range(len(tableau)):
    #le premier append permet d'ajouter l'image du pokémon réduite par le 
    #POKEMON_SIZE avec les coordonnées associés à la liste, qui est obtenue 
    #grâce au tableau csv original
    #Le 2ème append permet d'avoir en même temps un bouton combat de taille 
    #réduite pour chaque pokémon, les deux listes ont donc 151 éléments
    pokemon_img.append([pygame.transform.scale(pygame.image.load(os.path.join(images_pokemons, tableau[w][0] + ".png")), Taille_Pokemon),tableau[w][1]])
    boutons_combat.append(pygame.transform.scale(pygame.image.load('fight_button.png'),Taille_Bouton)) #Image de bouton dans le dossier du script, "fight_button"

# Position initiale du dresseur, choisie de telle sorte à être sur le chemin en haut à droite, mais peut être choisie différemment
dresseur_x = 1020
dresseur_y = 20

# Position map, choisie pour être centrée dans la fenêtre

carte_x = 10
carte_y = 10


#Fonction permettant de détecter lorsque la souris clique sur une zone cliquable
def button_clicked(zone_cliquable, position_souris, click_souris):
    if zone_cliquable.collidepoint(position_souris) and click_souris[0]:
        return True
    return False   

MIN_DISTANCE = 100 #Distance à partir de laquelle le pokémon s'affiche
DISTANCE_INTERACTION = 20 #Distance à partir de laquelle on peut lancer le combat en cliquant sur le bouton

derniere_direction_dresseur=None #Permet dans la boucle du jeu que lorsque le dresseur est immobile, il s'affiche quand même, et dans la dernière direction qu'il a pris lors du dernier déplacement

# Boucle du jeu
running = True 
while running: #Tant que running ne passe pas à False (échap ou tous les pokémons capturés), le jeu continue
    fenetre.fill(Blanc)  # Fond blanc, car le fond noir crée des bugs visuels
    
    # lorsque running passe à False, la fenêtre se ferme, le jeu s'arrête
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

    # afficher la carte
    fenetre.blit(carte, (carte_x, carte_y))
    # Contrôles du dresseur avec les flèches + ne peut pas sortir de la fenêtre (collisions)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if dresseur_x > 0:
           dresseur_x -= 0.05 #valeur du déplacement choisie empiriquement pour que le personnage soit ni trop lent ni trop rapide
    if keys[pygame.K_RIGHT]:
        if dresseur_x < largeur - dresseur_face.get_width():
            dresseur_x += 0.05
    if keys[pygame.K_UP]:
        if dresseur_y > 0:
           dresseur_y -= 0.05
    if keys[pygame.K_DOWN]:
        if dresseur_y < hauteur - dresseur_face.get_height():
           dresseur_y += 0.05
           
    # Déterminez la direction du déplacement du dresseur en fonction des touches enfoncées
    direction_dresseur = None
    if keys[pygame.K_LEFT]:
       direction_dresseur = 'gauche'
    elif keys[pygame.K_RIGHT]:
       direction_dresseur = 'droite'
    elif keys[pygame.K_UP]:
       direction_dresseur = 'haut'
    elif keys[pygame.K_DOWN]:
       direction_dresseur = 'bas'

    # Si aucune touche de déplacement n'est enfoncée, on conserve la dernière direction du dresseur ou on utilise une direction par défaut dans le cas de l'initialisation du jeu
    #Cette partie permet d'afficher le dresseur même lorsque il est immobile
    if direction_dresseur is None:
        if derniere_direction_dresseur is not None:
           direction_dresseur = derniere_direction_dresseur
        else:
           direction_dresseur = 'bas'  # Par défaut, le dresseur regarde vers le bas à l'initialisation

    # On utilise l'image appropriée du dresseur en fonction de la direction qu'il prend
    if direction_dresseur == 'gauche':
      fenetre.blit(dresseur_gauche, (dresseur_x, dresseur_y))
    elif direction_dresseur == 'droite':
       fenetre.blit(dresseur_droite, (dresseur_x, dresseur_y))
    elif direction_dresseur == 'haut':
       fenetre.blit(dresseur_dos, (dresseur_x, dresseur_y))
    elif direction_dresseur == 'bas':
       fenetre.blit(dresseur_face, (dresseur_x, dresseur_y))

    # On met à jour la dernière direction du dresseur
    derniere_direction_dresseur = direction_dresseur

    
    
    #afficher les pokémons
    for i in range(len(tableau)): #On parcourt tous les pokémons et leurs coordonnées
         nom_pokemon=tableau[i][0]
         
         #Coordonnées des pokémons sur la fenêtre
         pokemon_x = tableau[i][1][0]*largeur/42 #Facteur supplémentaire pour permettre d'adapter les coordonnées des pokémons définies à part à celles de la fenêtre
         pokemon_y = tableau[i][1][1]*hauteur/11 #42 et 11 choisis empiriquement pour que tous les pokémons (151) rentrent sur la map et la recouvre globalement
         
         #initialiser une distance 
         carteTemp = Map([dresseur_x,dresseur_y], tableau, MIN_DISTANCE)
         
         #On affiche les pokémons si ils sont suffisamment près au sens de MIN_DISTANCE, on utlise la classe Map et la fonction distance du module importé
         if carteTemp.distance([pokemon_x,pokemon_y],[dresseur_x,dresseur_y]) < MIN_DISTANCE:    
             fenetre.blit(pokemon_img[i][0], (pokemon_x,pokemon_y)) #Ca marche car pokémons dans le même ordre dans tableau et pokemon_img, on affiche donc l'image du pokémon à sa position
          
         #Dans toute cette condition, le joueur est assez proche pour lancer le combat, au sens de DISTANCE_INTERACTION
         if carteTemp.distance([pokemon_x,pokemon_y],[dresseur_x,dresseur_y]) < DISTANCE_INTERACTION:
             
             # Afficher l'image du bouton "Combat"
             bouton_combat_largeur = boutons_combat[i].get_width()
             bouton_combat_hauteur = boutons_combat[i].get_height()
             fenetre.blit(boutons_combat[i], (pokemon_x + Taille_Pokemon[0] // 2 - bouton_combat_largeur // 2, pokemon_y - 20)) #On affiche le bouton de combat propre à ce pokémon via la liste de boutons, la position est choisie empiriquement pour être bien placée par rapport au pokémon

             # Définir la zone cliquable permettant d'engendrer le combat
             activation_bouton = pygame.Rect(pokemon_x + Taille_Pokemon[0] // 2 - bouton_combat_largeur // 2, pokemon_y-5, bouton_combat_largeur, 20) #Position choisie pour se superposer à l'image du bouton
   
             # Actions à réaliser lorsque la souris clique sur la zone 
             #d'activation du bouton combat
             for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                 position_souris = pygame.mouse.get_pos()
                 click_souris = pygame.mouse.get_pressed()
                 if button_clicked(activation_bouton, position_souris, click_souris): #Si la souris clique sur le bouton combat
                    choix = ''
                    while choix not in Dresseur.pokemonDeDepart:
                        print(Dresseur.pokemonDeDepart)
                        choix = input("Choix du pokémon pour combattre parmis ceux possédés :")
                    #Alors le combat se lance via la fonction définie dans la classe Dresseur
                    pygame.mixer.stop() #On arrête la musique pour pas qu'elle se superpose à celle du combat
                    
                    dresseur = Dresseur([dresseur_x,dresseur_y],DISTANCE_INTERACTION)
                    p1_attributs = Pokemons().pokemons[choix]
                    p1 = PokemonDresseur(p1_attributs.nom, p1_attributs.type1, p1_attributs.type2, p1_attributs.barreDeVie, p1_attributs.attack, p1_attributs.defense)
                    p2_attributs = Pokemons().pokemons[nom_pokemon]
                    p2 = PokemonSauvage(p2_attributs.nom, p2_attributs.Coord, p2_attributs.type1, p2_attributs.type2, p2_attributs.barreDeVie, p2_attributs.attack, p2_attributs.defense)
                    
                    print(p1.nom, "barredevie", p1.barreDeVie, "def", p1.defense)
                    print("attaque", p2.attack, "def", p2.defense)
                    
                    #le combat se lance
                    
                    combat = Combat(p1, p2)
                    #fenetre de type
                    # pygame.surface.Surface
                    
                    issue_combat = combat.lancement_combat() #lance le combat
                    
                    #fermer la carte en attendant que le combat se déroule
                    
                    if issue_combat == 'Victoire' :
                        #Si le pokémon n'est pas déjà présent dans la liste de ceux possédés, l'ajouter (utile pour le pokémon starter pour pas l'avoir en double)
                        if tableau[i][0] not in Dresseur.pokemonDeDepart:
                           Dresseur.pokemonDeDepart.append(nom_pokemon) #rajouter le pokémon vaincu au starter
                      
                           print(Dresseur.pokemonDeDepart) #Contrôle visuel de l'ajout dans la liste
                        
                           # Rendre le Pokémon transparent à défaut de pouvoir supprimer son affichage une fois vaincu
                           pokemon_img[i][0].set_alpha(0)
                      
                           # Même chose pour le bouton combat qui lui est associé 
                           boutons_combat[i].set_alpha(0)
                 #Reste le cas de si il appuie sur FUITE, relancer la musique de la map
                  
    # Mise à jour de l'affichage
    pygame.display.update()
    
    #Le jeu se ferme si le joueur appuie sur ECHAP
    if keys[pygame.K_ESCAPE]:
        running=False
        
    #Fin du jeu, tous les pokémons sont possédés, le jeu se ferme
    if len(Dresseur.pokemonDeDepart)==151:
        print("Fin du jeu")
        running=False

pygame.quit() #Ferme la fenêtre du jeu
           