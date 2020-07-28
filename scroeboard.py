import pygame.font 
from pygame.sprite import Group
from ship import Ship

class ScroeBoard():
    def __init__(self,screen,status,ai_setting):
        self.screen = screen
        self.status = status
        self.ai_setting = ai_setting

        self.screen_rect = screen.get_rect()

        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()
    
    def prep_score(self):
        round_score = int(round(self.status.score,-1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,
            self.text_color,self.ai_setting.bg_color)
        
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.ai_setting.Screen_width-10
        self.score_image_rect.top = 10
    
    def prep_high_score(self):
        high_score_str = "{:,}".format(self.status.high_score)
        self.high_score_image = self.font.render(high_score_str,True,
            self.text_color,self.ai_setting.bg_color)
        
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_image_rect.top

    def prep_level(self):
        level_str = "{:,}".format(self.status.level)
        self.level_image = self.font.render(level_str,True,
            self.text_color,self.ai_setting.bg_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom+10

    def prep_ship(self):
        self.ships = Group()
        for number in range(self.status.ship_left):
            ship = Ship(self.screen,self.ai_setting)
            ship.rect.left = 10+number*ship.rect.width
            ship.rect.top = self.score_image_rect.top
            self.ships.add(ship)


    def blitme(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        for ship in self.ships.sprites():
            ship.blitme()
