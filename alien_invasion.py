import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化游戏并创建屏幕
    pygame.init()
    ai_settings = Settings()#导入settings模块中的设置
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建飞船.创建存储子弹的编组,创建一个外星人
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens)

    #开启游戏主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()