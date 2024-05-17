# Pokémon: projet informatique

### Dans le répertoire "Projet Pokémon", vous avez:

* le fichier main.py qui contient le code nécessaire pour lancer le jeu et effectuer un combat, bien qu'un problème n'ait pas été résolu concernant le retour de la fenêtre de la carte après la fin du combat.

* le fichier Menu.py qui contient également le jeu, avec un menu qui se lance au début mais ne permet pas de lancer de combats, nous n'avons pas trouvé le problème puisque l'appel au combat se fait de la même manière que dans main.py mais n'aboutit pas

* un fichier Pokemon.py dans lequel ont été définies toutes les classes concernant les Pokemons

* un fichier ClassesMapDresseur.py dans lequel les classes Map et Dresseur ont été définies

* un fichier combat_code.py dans lequel la classe combat a été définie

* deux fichiers csv pokemon_coordinates.csv et pokemon_first_gen.csv contenant les données sur les pokémons, que nous avons utilisées dans notre code

* un fichier player_turn.py dans lequel est initialisée l'interface de combat utilisée, ainsi qu'un fichier player_turn.ui qui lui est associé et qui permet de modifier l'interface à partir de Qt Designer

* deux fichiers ressources_combat.py et ressources_combat.qrc  qui sont nécessaires au fonctionnement de l'interface graphique liée aux combats




### Pour les fichiers sonores et les images, vous avez :

* musique_map et le dossier music qui contiennent la musique qui est jouée lorsque la carte est ouverte et lorsqu'un combat est en cours

* une image map qui correspond au fond de carte utilisé pour le jeu

* des images dresseur_gauche, dresseur_face, dresseur_droite, dresseur_dos qui sont les images utilisées pour afficher le dresseur sur la carte selon sa direction

* une image fight_button qui s'affiche sur la carte lorsque le joueur s'approche suffisamment d'un pokémon

* une image logo_pokemon qui est présente sur le menu du jeu

* un dossier Pokemons_pic qui contient les images des pokémons tels qu'ils s'affichent sur la carte

* un dossier pokemons qui contient les images des pokémons tels qu'ils s'affichent dans les combats

* deux dossier boxes et background qui contiennent respectivement le cadre dans lequel sont affichés les noms et les PV des pokémons en combat, et l'image de fond des combats.

### Le jeu :

Selon le code lancé, il y a ou non un menu au jeu, à partir duquel il est possible de lancer une partie.
Le joueur contrôle alors un dresseur qui peut se déplacer sur la carte. Lorsqu'il s'approche suffisamment d'un pokémon, son image apparaît également sur la carte, et un bouton "Fight" également lorsque le joueur s'en rapproche davantage. 
En cliquant sur ce bouton, un combat se lance et le joueur doit choisir un pokémon dans ceux de son inventaire (écrire son nom dans la console) pour l'affrontement.
Le combat propose trois actions pour le joueur : la fuite fait quitter le combat, les deux types d'attaque permettent d'affaiblir l'adversaire, qui lui même attaquera après.
Si le joueur perd, il revient sur la carte. S'il gagne, il capture le pokémon s'il ne le possède pas déjà et peut l'utiliser dans de futurs combats.
Le jeu prend fin lorsque les 151 pokémons ont été capturés.




* Par Anthony EVRARD, Aitor LOPEZ et Gaëlle SAINT-PAUL
