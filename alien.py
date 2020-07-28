import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_setting,screen):
        super().__init__()

        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.ai_setting.alien_move_speed
                        *self.ai_setting.alien_move_dirc)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)
