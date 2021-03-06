import sys
import pygame
from bullet import Buttel
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        #创建子弹，将其添加入编组中
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果子弹没有达到上限，则发射一颗子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Buttel(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,ship,buttels):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,buttels)
        

def update_screen(ai_setting,screen,ship,alien,bullets):
    '''更新屏幕图案，刷新屏幕'''
    #重绘屏幕
    screen.fill(ai_setting.bg_color)
    #在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)

    #显示屏幕
    pygame.display.flip()

def update_bullets(bullets):
    "更新子弹位置，并删除已消失子弹"
    #更新子弹位置
    bullets.update()

    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(ai_settings,screen,aliens):
    '''创建外星人群'''
    #创建一个外星人，并计算一行可容纳多少外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space_x / (2*alien_width))

    #创建第一行外星人
    for alien_number in range(number_alien_x):
        #创建一个外星人并加入当前行
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        aliens.add(alien)