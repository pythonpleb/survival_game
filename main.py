import pygame

from background import build_background
from manager import draw_player
from player import Player
from lighting import create_light

pygame.init()
running = True
clock = pygame.time.Clock()

p = Player(900, 500, 0, 0)  # spawn player at 900, 500 with a change of 0 for x and y


def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # esc button closes the game
                running = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                p.player_x_change = -p.move_speed  # assign the change

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                p.player_x_change = p.move_speed

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                p.player_y_change = -p.move_speed

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                p.player_y_change = p.move_speed

        if event.type == pygame.KEYUP:
            p.player_x_change = 0  # stop moving player if key is not pressed anymore
            p.player_y_change = 0

    # change player position
    p.player_x += p.player_x_change
    p.player_y += p.player_y_change


def main():
    events()
    build_background()
    draw_player(p)  # pass player object into this method
    create_light()
    pygame.display.flip()
    clock.tick(50)


if __name__ == '__main__':
    while running:
        main()
    pygame.quit()
