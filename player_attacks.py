import pygame

from background import screen

player_swing = False

swing_animation = [#pygame.image.load('melee/swing4.png').convert_alpha(),
                   #pygame.image.load('melee/swing4.png').convert_alpha(),
                   #pygame.image.load('melee/swing5.png').convert_alpha(),
                   #pygame.image.load('melee/swing5.png').convert_alpha(),
                   #pygame.image.load('melee/swing6.png').convert_alpha(),
                   #pygame.image.load('melee/swing6.png').convert_alpha(),
                   pygame.image.load('melee/swing7.png').convert_alpha(),
                   pygame.image.load('melee/swing7.png').convert_alpha(),
                   pygame.image.load('melee/swing8.png').convert_alpha(),
                   pygame.image.load('melee/swing8.png').convert_alpha(),
                   pygame.image.load('melee/swing9.png').convert_alpha(),
                   pygame.image.load('melee/swing9.png').convert_alpha(),
                   pygame.image.load('melee/swing10.png').convert_alpha(),
                   pygame.image.load('melee/swing10.png').convert_alpha(),
                   pygame.image.load('melee/swing11.png').convert_alpha(),
                   pygame.image.load('melee/swing11.png').convert_alpha(),
                   pygame.image.load('melee/swing12.png').convert_alpha(),
                   pygame.image.load('melee/swing12.png').convert_alpha(),
                   pygame.image.load('melee/swing13.png').convert_alpha(),
                   pygame.image.load('melee/swing13.png').convert_alpha(),
                   ]
frame_count = 0
swing_cooldown = 11


# pass True if player pressed f (from main.py)
def swing_status(status):
    global player_swing

    if status:
        player_swing = True
    else:
        player_swing = False


def player_melee(p):
    global swing_cooldown
    global frame_count
    global player_swing
    if swing_cooldown <= 0:  # at 0 turn off swing animation and reset cooldown
        player_swing = False
        swing_cooldown = 11
        frame_count = 0

    if swing_cooldown > 0:
        if player_swing:
            screen.blit(swing_animation[frame_count], (p.player_x + 17, p.player_y + 17))
            swing_cooldown -= 1  # countdown



    frame_count += 1
    if frame_count + 1 > 14:  # 10 frames to cycle through
        frame_count = 0
