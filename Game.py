import pygame
import random
import math
from User_Tank import *
from Enemy import *
# initialize game
pygame.init()

# screen of the game
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space War")

# handles closing of game
running = True

#actors in the game
actors = []

score = 0
font = pygame.font.Font("freesansbold.ttf",32)
text_x = 10
text_y = 10

def show_health(health):
    health_text = font.render("Health: " + str(health) ,True,(255,255,255))
    screen.blit(health_text, (200, 10))

def show_score(x,y):
    score_text  = font.render("Score: " + str(score) ,True,(255,255,255))
    screen.blit(score_text,(x,y))


def isCollide(x1,y1,x2,y2):
    dist = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    if dist < 27:
        return True
    else:
        return False
def randomlol():
    print("COLLIDED")

def enemy_hit(score):
    score += 1
    return score

    

def isBulletToEnemyCollision(x1,y1,x2,y2):

    return isCollide(x1,y1,x2,y2)


def BulleytoEnemyCollision(x1,y1,enemies):
    global score
    for i in enemies:
        if isCollide(x1,y1,i.x_pos,i.y_pos) is True:
            i.got_shot()
            if i.health == 0:
                score += 1
                enemies.remove(i)
                actors.remove(i)
            return True

    return False

game_end = True
def end_game():
    global game_end
    global enemies
    global actors
    global level
    global score
    global user_tank
    user_tank.health = 200
    level = 1
    text = font.render("Click any key to play again. Click mouse to end game.", True, (255, 255, 255))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (300, 200))
    screen.blit(text, (50,300))

    score = 0
    enemies.clear()
    new_actors = []
    for i in actors:
        if type(i) is not Enemy:
            new_actors.append(i)
    actors = new_actors
    game_end = False
    pass

def draw():
    x = 0
    if game_end == False:
        end_game()
        return
    for i in actors:
        if i.fired == True:
            i.bullet.update_loc()
            if i.bullet.fired == False:
                i.fired = False
            else:
                if type(i) is UserTank:
                    x+=1
                elif isCollide(i.bullet.x_pos,i.bullet.y_pos,user_tank.x_pos,user_tank.y_pos):
                    user_tank.get_shot()
                    i.bullet.fired = False
                    if user_tank.health == 0:
                        end_game()
                        break
                if type(i) == Enemy:
                    x+=1
                elif BulleytoEnemyCollision(i.bullet.x_pos,i.bullet.y_pos,enemies) is True: #have to add all the enemies
                    i.hit_enemy()

                    i.bullet.fired = False
                    randomlol()
                screen.blit(i.bullet.img,(i.bullet.x_pos,i.bullet.y_pos))
        screen.blit(i.img,(i.x_pos,i.y_pos))

# User Tank object
user_tank = UserTank()
actors.append(user_tank)
enemies = []

def enemy_move():
    for i in enemies:
        i.move()

level = 1

def create_level(n):
    global level
    for i in range(n):
        enemy = Enemy()
        actors.append(enemy)
        enemies.append(enemy)
    level+=1
def check_enemies_dead():
    global level
    if len(enemies) == 0:
        level += 1
        return True
def enemy_shoot(x,y):
    global enemies
    for i in enemies:
        if i.fired is False:
            i.shoot(x,y)


# Game loop
while running:
    # RGB color
    if game_end is False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game_end = True
            if event.type == pygame.MOUSEBUTTONUP:
                running = False

    if check_enemies_dead() is True:
        user_tank.replenish_health()
        create_level(level)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move left
                user_tank.move_left()
            if event.key == pygame.K_RIGHT:  # move right
                user_tank.move_right()
            if event.key == pygame.K_UP:  # move up
                user_tank.move_up()
            if event.key == pygame.K_DOWN:
                user_tank.move_down()
        if event.type == pygame.KEYUP:  # keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==  pygame.K_DOWN or event.key == pygame.K_UP:
                user_tank.reset_change()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if user_tank.fired == False:
                user_tank.shoot(pos[0], pos[1])



    #DRAW USER TANK
    enemy_shoot(user_tank.x_pos,user_tank.y_pos)
    user_tank.update_location()
    enemy_move()
    draw()
    show_score(text_x,text_y)
    show_health(user_tank.health)
    pygame.display.update()
