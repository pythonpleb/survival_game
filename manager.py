import pygame

from background import screen

player_animation_right = [pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          ]
player_animation_left = [pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         ]
player_animation_up = [pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       ]
player_animation_down = [pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         ]

frame_count = 0

player_standing_still_right = pygame.image.load('player/player_walk1_r.png').convert_alpha()
player_standing_still_left = pygame.image.load('player/player_walk1_l.png').convert_alpha()
player_standing_still_up = pygame.image.load('player/player_walk1_u.png').convert_alpha()
player_standing_still_down = pygame.image.load('player/player_walk1_d.png').convert_alpha()

right = False
left = False
up = False
down = False

still_right = False
still_left = False
still_up = True
still_down = False


def set_animation_status(right_status, left_status, up_status, down_status):
    global right
    global left
    global up
    global down
    global still_right
    global still_left
    global still_up
    global still_down

    if right_status:
        right = True
        left = False
        up = False
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if left_status:
        right = False
        left = True
        up = False
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if up_status:
        right = False
        left = False
        up = True
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if down_status:
        right = False
        left = False
        up = False
        down = True
        still_right = False
        still_left = False
        still_up = False
        still_down = False


def set_player_still_direction(right_status, left_status, up_status, down_status):
    global still_right
    global still_left
    global still_up
    global still_down

    global right
    global left
    global up
    global down

    if right_status:
        still_right = True
        still_left = False
        still_up = False
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if left_status:
        still_right = False
        still_left = True
        still_up = False
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if up_status:
        still_right = False
        still_left = False
        still_up = True
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if down_status:
        still_right = False
        still_left = False
        still_up = False
        still_down = True
        right = False
        left = False
        up = False
        down = False


# TODO: use array to blit animation when key pressed, change direction of animation, resize images
def draw_player(p):
    global frame_count
    # screen.blit(player_standing_still_right, (p.player_x, p.player_y))
    if right:
        screen.blit(player_animation_right[frame_count], (p.player_x, p.player_y))
    if left:
        screen.blit(player_animation_left[frame_count], (p.player_x, p.player_y))
    if up:
        screen.blit(player_animation_up[frame_count], (p.player_x, p.player_y))
    if down:
        screen.blit(player_animation_down[frame_count], (p.player_x, p.player_y))
    if still_right:
        screen.blit(player_standing_still_right, (p.player_x, p.player_y))
    if still_left:
        screen.blit(player_standing_still_left, (p.player_x, p.player_y))
    if still_up:
        screen.blit(player_standing_still_up, (p.player_x, p.player_y))
    if still_down:
        screen.blit(player_standing_still_down, (p.player_x, p.player_y))

    frame_count += 1
    if frame_count + 1 > 30:  # 30 frames to cycle through
        frame_count = 0
