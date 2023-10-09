import pygame
from pygame import Vector2
from math import cos,sin

WIDTH = 1280
HEIGHT = 720

window = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

game_running = True
angle_moon = 0
pos = Vector2(WIDTH/2,HEIGHT/2)
while game_running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False 

    keys = pygame.key.get_pressed()

    dt = clock.tick()/1000

    if keys[pygame.K_w]:
        pos.y -= 200*dt

    angle_moon += dt
    rad = 50
    dist_moon = 300
    moon_size = 30
    pos_moon = pos + dist_moon * Vector2(cos(angle_moon),sin(angle_moon))

    pygame.draw.circle(window,[255,0,0],pos,rad)
    pygame.draw.circle(window,[0,255,0],pos_moon,moon_size)

    pygame.display.update()