# -*- coding:utf-8 -*-

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个子弹的编组、一个外星人的编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 检查玩家的输入
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船的位置
        ship.update()
        # 更新未消失的子弹位置
        gf.update_bullets(bullets)
        # 更新外星人的位置
        gf.update_aliens(ai_settings, aliens)
        # 使用更新后的位置来绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
