# On importe le module
import pygame
from player import Player
from game import Game


# On initialise
pygame.init()

# On crée la fenêtre
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Shooter")

# On gère le framerate
clock = pygame.time.Clock()

# On gère l'arrière plan
background = pygame.image.load('./assets/principal.png')

# On crée l'instance du jeu
game = Game()

running = True
while running:

    screen.blit(background, (0,0))
       
    game.update(screen)
    # On vérifie si le jeu a commencé
    # if game.is_playing:
        # On déclenche les instructions de la partie
    # On vérifie si le jeu n'a pas commencé
    # else:
    #     # On ajoute l'écran de bienvenue
    #     screen.blit(play_button, play_button_rect)
    #     screen.blit(banner, banner_rect)

    # On met à jour l'écran
    pygame.display.flip()

    # On applique le 60 fps
    clock.tick(60)

    for event in pygame.event.get():

        # On vérifie tous les évènements pour gérer la fermeture de la fenêtre
        # On quitte le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # On détécte les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # On détecte si la touche espace est appuyée
            # if event.key == pygame.K_SPACE:
            #     if game.is_playing:
            #         game.player.launch_projectile()
            #     else:
            #         game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        # on vérifie si on clique sur le bouton play avec la souris
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            # # On vérifie si on a la souris sur le bouton play
            # if play_button_rect.collidepoint(event.pos):
            #     # On met le jeu en mode lancer
            #     game.start()
            #     # jouer le son
            #     game.sound_manager.play('click')