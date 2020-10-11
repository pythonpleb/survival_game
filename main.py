import pygame

from background import build_background
from lighting import create_light
from manager import draw_player, set_animation_status, set_player_still_direction
from player import Player

pygame.init()
running = True
clock = pygame.time.Clock()

p = Player(870, 500, 0, 0)  # spawn player at 900, 500 with a change of 0 for x and y


def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # esc button closes the game
                running = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                p.player_x_change = -p.move_speed  # assign the change
                set_animation_status(False, True, False, False)  # pass animation status into manager.py

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                p.player_x_change = p.move_speed
                set_animation_status(True, False, False, False)

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                p.player_y_change = -p.move_speed
                set_animation_status(False, False, True, False)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                p.player_y_change = p.move_speed
                set_animation_status(False, False, False, True)

        if event.type == pygame.KEYUP:
            p.player_x_change = 0  # stop moving player if key is not pressed anymore
            p.player_y_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                set_player_still_direction(False, True, False, False)

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                set_player_still_direction(True, False, False, False)

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                set_player_still_direction(False, False, True, False)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                set_player_still_direction(False, False, False, True)

            set_animation_status(False, False, False, False)  # just in case

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
