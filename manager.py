import pygame

from background import screen


# TODO: use array to blit animation, resize images
def draw_player(p):
    player_img = pygame.image.load('player/player_walk1.png')
    screen.blit(player_img, (p.player_x, p.player_y))
