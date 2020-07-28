import sys
import pygame
import json
from time import sleep
from setting import Settings
from bullet import Bullet
from alien import Alien

def check_keydown_even(even,ai_setting,status,screen,button,ship,bullets):
    if even.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif even.key == pygame.K_LEFT:
        ship.moving_left = True
    elif even.key == pygame.K_DOWN:
        ship.moving_down = True
    elif even.key == pygame.K_UP:
        ship.moving_up = True
    elif even.key == pygame.K_q:
        status.game_active = False
        pygame.mouse.set_visible(True)
    elif even.key == pygame.K_p:
        play_button_on(status,button)
    elif even.key == pygame.K_SPACE:
        if len(bullets) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)

def check_keyup_even(even,ship):
    if even.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif even.key == pygame.K_LEFT:
        ship.moving_left = False
    elif even.key == pygame.K_DOWN:
        ship.moving_down = False
    elif even.key == pygame.K_UP:
        ship.moving_up = False

def check_events(ai_setting,status,screen,ship,button,bullets):
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            with open('high_score.json','w') as jf:
                json.dump(status.high_score,jf)
            sys.exit()
        elif even.type == pygame.KEYDOWN:
            check_keydown_even(even,ai_setting,status,
                screen,button,ship,bullets)
        elif even.type == pygame.KEYUP:
            check_keyup_even(even,ship)
        elif even.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x,mouse_y):
                play_button_on(status,button)

def play_button_on(status,button):
    status.rest_stats()
    status.game_active = True
    pygame.mouse.set_visible(False)

def get_number_row(ai_setting,ship_height,alien_height):
    avalib_x = ai_setting.Screen_hight - 2*alien_height - ship_height
    row_number = int(avalib_x/(2*alien_height))
    return row_number

def get_number_alienx(ai_setting,alien_width):
    avalib_x = ai_setting.Screen_width - 2*alien_width
    column_number = int(avalib_x/(2*alien_width))
    return column_number

def creat_alien(ai_setting,screen,aliens,alien_number,row_number):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width+2*alien_number*alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2*row_number*alien_height
    aliens.add(alien)
    
def creat_fleet(ai_setting,screen,ship,aliens):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien_hight = alien.rect.height

    column_number = get_number_alienx(ai_setting,alien_width)
    row_numbers = get_number_row(ai_setting,ship.rect.height,alien_hight)

    for row_number in range(0,row_numbers):
        for alien_number in range(0,column_number):
            creat_alien(ai_setting,screen,aliens,alien_number,row_number)

def aliens_change_dirc(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.ai_setting.alien_dorp_speed
    alien.ai_setting.alien_move_dirc *= -1

def check_aliens_edge(ai_setting,status,screen,sb,ship,aliens,bullets):
    for alien in aliens.sprites():
        if alien.rect.right >= alien.ai_setting.Screen_width:
            aliens_change_dirc(aliens)
            break
        elif alien.rect.x <= 0:
            aliens_change_dirc(aliens)
            break
        elif alien.rect.bottom >= ai_setting.Screen_hight:
            ship_hit(ai_setting,status,screen,sb,ship,aliens,bullets)
            break

def check_aliens_bullet_collision(ai_setting,screen,status,sb,
    ship,aliens,bullets):

    collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collision:
        for aliens in collision.values():
            status.score += ai_setting.alien_point*len(aliens)
        if status.score > status.high_score:
            status.high_score = status.score
            sb.prep_high_score()
        sb.prep_score()
    if len(aliens)==0:#此时舰队被全部消灭，创建新舰队并提高等级
        bullets.empty()
        creat_fleet(ai_setting,screen,ship,aliens)
        ai_setting.increase_speed()
        status.level += 1
        sb.prep_level()

def ship_hit(ai_setting,status,screen,sb,ship,aliens,bullets):
    if status.ship_left > 0:
        status.ship_left -= 1
        sb.prep_ship()
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:#此时判定游戏失败
        game_over(ai_setting,status,screen,sb,ship,aliens,bullets)

def game_over(ai_setting,status,screen,sb,ship,aliens,bullets):
    pygame.mouse.set_visible(True)
    ai_setting.initialize_dynamic_setting()
    status.rest_stats()

    aliens.empty()
    bullets.empty()
    creat_fleet(ai_setting,screen,ship,aliens)
    ship.center_ship()

    sb.prep_score()
    sb.prep_level()
    sb.prep_ship()

def updata_aliens(ai_setting,status,screen,sb,ship,aliens,bullets):
    aliens.update()
    check_aliens_edge(ai_setting,status,screen,sb,
        ship,aliens,bullets)

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting,status,screen,sb,ship,aliens,bullets)

def updata_bullets(ai_setting,screen,status,sb,ship,aliens,bullets):
    for bullet in bullets.copy():
        bullet.updata()
        if bullet.y <= 0:
            bullets.remove(bullet)
    check_aliens_bullet_collision(ai_setting,screen,status,sb,
        ship,aliens,bullets)
        
def updata_screen(ai_setting,status,screen,sb,ship,button,bullets,aliens):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    sb.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien in aliens.sprites():
        alien.blitme()
    if not status.game_active:
        button.draw_button()
    pygame.display.flip()