import pygame
import sys
sys.path.append(".")
from setting import Settings
from ship import Ship
import game_funcion as gf

def run_game():
    #初始化屏幕
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.Screen_width,ai_settings.Screen_hight))
    ship = Ship(screen,ai_settings)
    pygame.display.set_caption('Alien Invasion')

    #游戏主循环
    while True:
        for evens in pygame.event.get():
            if evens.type == pygame.QUIT:
                sys.exit()
            elif evens.type == pygame.KEYDOWN:
                print(evens.key)
        gf.updata_screen(ai_settings,screen,ship)
        
run_game()


