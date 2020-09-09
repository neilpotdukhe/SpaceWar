import pygame
import random
from Bullet import *

class Enemy:
    def __init__(self):
        x_positions = [0,800]
        y_positions = [0,600]
        self.x_pos = x_positions[random.randint(0,1)]
        self.y_pos = y_positions[random.randint(0,1)]
        self.x_change = 0
        self.y_change = 0
        self.img = pygame.image.load("enemy.png")
        self.bullet = Bullet()
        self.fired = False
        self.health = 100
        self.bullet.tank = "Enemy"

    def move_left(self):
        self.x_change = -8

    def move_right(self):
        self.x_change = 8

    def move_up(self):
        self.y_change = -8

    def move_down(self):
        self.y_change = 8

    def reset_change(self):
        self.x_change = 0
        self.y_change = 0

    def update_location(self):
        self.x_pos += self.x_change
        self.y_pos += self.y_change

        if self.x_pos <= 0:
            self.x_pos = 0
        elif self.x_pos >= 790:
            self.x_pos = 790
        if self.y_pos <= 0:
            self.y_pos = 0
        elif self.y_pos >= 580:
            self.y_pos = 580

    def move(self):
        ran = random.randint(1, 4)
        if ran == 1:
            self.move_left()
            self.move_down()
        elif ran == 2:
            self.move_left()
            self.move_up()
        elif ran == 3:
            self.move_right()
            self.move_down()
        elif ran == 4:
            self.move_right()
            self.move_up()
        self.update_location()
    def got_shot(self):
        self.health -= 50
        if self.health == 50:
            self.img = pygame.image.load("enemy_half_life.png")

    def shoot(self,x,y):
        self.bullet.x_pos = self.x_pos
        self.bullet.y_pos = self.y_pos
        self.fired = True
        self.bullet.shoot(x, y)
        if self.bullet.fired == False:
            self.fired = False

