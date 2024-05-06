# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:28:53 2024

@author: Formation
"""


import tkinter as tk

fenetre = tk.Tk()

fond = tk.PhotoImage(file = 'E:/projet info/pokemons/background1.png')
pokemon1 = tk.PhotoImage(file = 'E:/projet info/pokemons/charmander.png')

#fond.paste(pokemon1, (20,20))

label = tk.Label(fenetre, image = fond)
label.pack()

label = tk.Label(fenetre, image = pokemon1)

label.pack()

#zone_dessin = tk.Canvas(fenetre, width=1299, height=620, bg = 'yellow')
#zone_dessin.tk.create_image(650, 300, image=pokemon1)

fenetre.mainloop()

