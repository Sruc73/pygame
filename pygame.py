import pygame
from pygame.locals import *

pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("data/background.jpg").convert()
fenetre.blit(fond, (0, 0))

#Chargement et collage du personnage
perso = pygame.image.load("data/perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#Gestion du déplacement lorsque l'on garde la touche enfoncée
# 400 est le délai avant de continuer les déplacements quand la touche reste enfoncée (en ms)
# 30 est le temps entre chaque déplacements (en ms)
pygame.key.set_repeat(400, 30)

#Boucle infinie
continuer = 1
while continuer:
    for event in pygame.event.get(): #Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN: #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0, 3)
            elif event.key == K_UP: #Si "flèche haute"
                #on monte le perso
                position_perso = position_perso.move(0, -3)
            elif event.key == K_LEFT: #Si "flèche gauche"
                #On va à gauche
                position_perso = position_perso.move(3, 0)
            elif event.key == K_RIGHT: #Si "flèche droite"
                #On va à droite
                position_perso = position_perso.move(-3, 0)

#Re-collage
fenetre.blit(fond, (0,0))
fenetre.blit(perso, position_perso)
#Rafraichissement
pygame.display.flip()
