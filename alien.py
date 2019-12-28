import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像并设置其rect属性
        self.image = pygame.image.load(r'D:\我的文件\pygame\images\alien.png')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.x = self.rect.width
        self.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect) 