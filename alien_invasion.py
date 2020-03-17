# -*- coding:utf-8 -*-

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


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

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        # 检查玩家的输入
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船的位置
            ship.update()
            # 更新未消失的子弹位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人的位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 使用更新后的位置来绘制新屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
