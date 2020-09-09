import pygame
import random
from User_Tank import *
import math


class Bullet:
    def __init__(self):

        self.x_pos = 0
        self.y_pos = 0
        self.x_change = 0
        self.y_change = 0
        self.img = pygame.image.load("Bullet.png")
        self.fired = False
        self.tank = ""

    def shoot(self,enemy_x,enemy_y):
        self.fired = True

        if self.tank == "Enemy":
            self.x_change = (enemy_x - self.x_pos) / 100
            self.y_change = (enemy_y - self.y_pos) / 100
        else:
            self.x_change = (enemy_x - self.x_pos) / 10
            self.y_change = (enemy_y - self.y_pos) /10
    def update_loc(self):
        if self.x_pos <= 0 or self.x_pos >= 800 or self.y_pos <= 0 or self.y_pos >= 600:
            self.fired = False
        self.x_pos += self.x_change
        self.y_pos += self.y_change
