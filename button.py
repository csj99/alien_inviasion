import pygame.font 

class Button():
    def __init__(self,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.text_color = (255,255,255)
        self.button_color = (0,255,0)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery
        
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
