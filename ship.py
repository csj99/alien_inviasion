import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_setting):
        super().__init__()

        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def updata(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_setting.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_setting.ship_speed_factor
        elif self.moving_up and self.rect.bottom > self.screen_rect.top:
            self.bottom -= self.ai_setting.ship_speed_factor
        
        self.rect.bottom = self.bottom
        self.rect.centerx = self.center

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
