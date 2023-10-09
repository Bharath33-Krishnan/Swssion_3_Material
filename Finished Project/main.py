import pygame
from pygame import Vector2
from math import cos, sin, radians
from copy import copy
from random import randint

from player import Player
from bullet import Bullet
from enemy import Enemy

WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode([WIDTH, HEIGHT])

FPS = 60
clock = pygame.time.Clock()

game_is_running = True

pl = Player(Vector2(WIDTH//2, HEIGHT//2))
bullets = []
enemies = []

for i in range(10):
    enemies.append(
        Enemy(WIDTH, HEIGHT)
    )

while game_is_running:
    window.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            angle = radians(pl.get_mouse_angle())
            dir = Vector2(cos(angle), sin(angle))
            bullets.append(Bullet(copy(pl.pos), dir))
            pl.shoot(window, enemies, WIDTH)

    keys = pygame.key.get_pressed()
    dt = clock.tick() / 1000

    if keys[pygame.K_LEFT]:
        pl.move_left(dt)
    if keys[pygame.K_RIGHT]:
        pl.move_right(dt)
    if keys[pygame.K_UP]:
        pl.move_up(dt)
    if keys[pygame.K_DOWN]:
        pl.move_down(dt)


    pl.update()
    pl.show(window)

    for bullet in bullets:
        if (bullet.pos - Vector2(WIDTH/2, HEIGHT/2)).magnitude() > WIDTH:
            bullets.remove(bullet)
        bullet.update(dt)
        bullet.show(window)

    for enemy in enemies:
        enemy.update(dt)
        enemy.show(window)

    pygame.display.update()
