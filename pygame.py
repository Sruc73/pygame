import pygame
from pygame.locals import *

pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("data/background.jpg").convert()
fenetre.blit(fond, (0, 0))

perso = pygame.image.load("data/perso.png").convert_alpha()
fenetre.blit(perso, (200, 300))

#Rafraîchissement de l'écran
pygame.display.flip()

#Boucle infinie
continuer = 1
while continuer:
    for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
        if event.type == QUIT: #Si un de ces événements est de type QUIT
            continuer = 0 #On arrête la boucle
