from random import randint
import pygame

class Enemy:
    def __init__(self, max_width, max_height):
        self.max_width, self.max_height = max_width, max_height
        self.pos = pygame.Vector2(randint(0, max_width), randint(0, max_height))
        self.vel = pygame.Vector2(0, 0)

        self.surface = pygame.Surface((50, 50))
        self.surface.fill((100, 100, 200))
        self.rect = self.surface.get_rect()

    def set_target(self, player_pos):
        pass

    def update(self, dt):
        self.pos += self.vel * dt

        self.rect.centerx = int(self.pos.x)
        self.rect.centery = int(self.pos.y)

    def show(self, surface):
        surface.blit(self.surface, self.rect)

    def reset(self):
        self.pos = pygame.Vector2(randint(0, self.max_width), randint(0, self.max_height))
