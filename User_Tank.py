import pygame
import random
from Bullet import *

class UserTank():
    def __init__(self):
        self.x_pos = 200
        self.y_pos = 400
        self.x_change = 0
        self.y_change = 0
        self.img = pygame.image.load("transportation.png")
        self.bullet = Bullet()
        self.fired = False
        self.score = 0
        self.bullet.tank = "User Tank"
        self.health = 200
    def move_left(self):
        self.x_change = -5

    def move_right(self):
        self.x_change = 5

    def move_up(self):
        self.y_change = -5

    def move_down(self):
        self.y_change = 5

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
    def shoot(self,x,y):
        self.bullet.x_pos = self.x_pos
        self.bullet.y_pos = self.y_pos
        self.fired = True
        self.bullet.shoot(x,y)
        if self.bullet.fired == False:
            self.fired = False

    def hit_enemy(self):
        self.score+=1

    def get_shot(self):
        self.health -= 50
    def replenish_health(self):
        self.health = 200