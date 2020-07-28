import sys
import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_funcion as gf
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scroeboard import ScroeBoard

def run_game():
    #初始化屏幕
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.Screen_width,ai_settings.Screen_hight))
    ship = Ship(screen,ai_settings)
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption('Alien Invasion')
    status = GameStats(ai_settings)
    #创建一个计分板
    scorebo = ScroeBoard(screen,status,ai_settings)

    #创建外星人舰队
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    #创建一个开始按键
    button = Button(screen,'Play')
    #游戏主循环
    while True:
        gf.check_events(ai_settings,status,screen,ship,button,bullets)
        if status.game_active:
            ship.updata()
            gf.updata_bullets(ai_settings,screen,status,scorebo,
                ship,aliens,bullets)
            gf.updata_aliens(ai_settings,status,screen,scorebo,
                ship,aliens,bullets)
        gf.updata_screen(ai_settings,status,screen,scorebo,
            ship,button,bullets,aliens)
        
run_game()
