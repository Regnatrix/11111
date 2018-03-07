'''
Sandra Dögg Kristmundsdóttir
20.02.2018
'''

import os
import random
import pygame
from pygame.locals import *
from random import *
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
litur = [255, 255, 255]
litur2 = [255, 255, 255]
rainbow = (randint(0,255), randint(0,255), randint(0,255))
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#music
pygame.mixer.music.load("maze.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

yes = True
maybe = True
while True:
    name1 = input("Nafn spilara: ")

    if len(name1) > 10:
        print("10 eða færri stafi takk")

    else:
        break
score1 = 10

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)
        global antibomb
        self.antibomb = 0
        self.defusedBombs = 0

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def draw(self):
        if self.antibomb >= 1:
            man = pygame.draw.rect(screen, (255, 200, 0), player.rect)
        else:
            man = pygame.draw.rect(screen, (255, 128, 0), player.rect)
        return man

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    print("Vinstri")
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    print("Hægri")
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    print("Toppur")
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    print("Botn")

        for bomb in bombs:
            if self.rect.colliderect(bomb.rect):
                if self.antibomb >= 1:
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = bomb.rect.left
                        bombs.remove(bomb)
                        self.defusedBombs -= 1
                        self.antibomb -= 1
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = bomb.rect.right
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibomb -= 1
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = bomb.rect.top
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibomb -= 1
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = bomb.rect.bottom
                        bombs.remove(bomb)
                        self.defusedBombs += 1
                        self.antibomb -= 1
                else:
                    raise SystemExit("Þú klesstir á")
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = bomb.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = bomb.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = bomb.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = bomb.rect.bottom
        for antibomb in antibombs:
            if self.rect.colliderect(antibomb.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.antibomb+=1
                    antibombs.remove(antibomb)
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.antibomb+=1
                    antibombs.remove(antibomb)
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.antibomb+=1
                    antibombs.remove(antibomb)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.antibomb+=1
                    antibombs.remove(antibomb)



# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Bomb(object):

    def __init__(self,pos):
        bombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class AntiBomb(object):

    def __init__(self, pos):
        antibombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

# Set up the display
pygame.display.set_caption("Maze")
screen = pygame.display.set_mode((960, 720))

clock = pygame.time.Clock()
walls = []  # List to hold the walls
bombs = []  # List to hold the bombs
antibombs = []
player = Player()  # Create the player


# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W      W     W     W        W                 WW",
    "WW  W  W  W  WWWW  W  WWWW  WWWW  WWWWWWW  W  WW",
    "WW  W     W     W     W  W        W        W  WW",
    "WW  WWWWWWWWAW  W  WWWW  WWWWWWWWWW  WWWWWWWWWWW",
    "WW     W        W     W           W     W     WW",
    "WW  WWWW  W  WWWWWWW  W  WWWW  W  W  W  WWWW  WW",
    "WW  W     W           W  B     W     W  W     WW",
    "WWWWW  WWWWWWWWWWWWWWWW  W  WWWWWWWWWW  W  WWWWW",
    "WW     W              W  W           W     W  WW",
    "WW  WWWW  WWWWWWWWWW  W  W  WWWW  WWWWWWWWWW  WW",
    "WW     W  W           W  W     W           W  WW",
    "WWWWW  W  WWWWWWWWWWWWW  WWWWWWWWWWWWWWWW  W  WW",
    "WW  W  W                 W        W        W  WW",
    "WW  W  WWWWWWW  WWWWWWWWWW  WWWWWWW  WWWW  W  WW",
    "WW     W        W     W  W     W     W     W  WW",
    "WWWWWWWB  WWWWWWW  W  W  W  WWWW  WWWW  WWWW  WW",
    "WW        W     W  W  W              W  W     WW",
    "WW  WWWWWWW  W  WWWW  WAWWWWWWWWWWW  W  W  WWWWW",
    "WW           W     W     W           W        WW",
    "WWWWWWWWWWWWWWWWW  W  W  W  WBWWWWWWWWWWWWWW  WW",
    "WW     W     W     W  W  W     W           W  WW",
    "WW  W  WWWW  W  WWWW  W  W  W  W  WWWWWWW  W  WW",
    "WW  W     W  W        W  W  W     W        W  WW",
    "WW  WWWW  W  WWWWWWWWWWWWW  WWWWWWW  WWWWWWW  WW",
    "WW     W     W              W        W     W  WW",
    "WW  W  WWWWWWWWWW  WWWW  WWWW  WWWAWWW  W  WWWWW",
    "WW  W        W     W        W           W     WW",
    "WW  WWWWWWW  W  WWWB  WWWWWWWWWWWWWWWWWWWWWW  WW",
    "WW        W     W     W                       EW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

]
# Lines
pygame.draw.line(screen, WHITE, (0, 70), (1000, 70))

# Text
name1Score = myfont.render(str(name1), True, (WHITE))
screen.blit(name1Score, (10, -5))
player1Score = myfont.render(str(score1), True, (WHITE))
screen.blit(player1Score, (25, 25))

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            endir = pygame.Rect(x, y, 16, 16)
        if col == "B":
            Bomb((x, y))
        if col == "A":
            AntiBomb((x, y))
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(endir):
        raise SystemExit("Þú vannst!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for bomb in bombs:
        pygame.draw.rect(screen, (255,0,255), bomb.rect)
    for antibomb in antibombs:
        pygame.draw.rect(screen, (50,150,120), antibomb.rect)

    pygame.draw.rect(screen, (0, 255, 255), endir)
    counter = 0
    if counter %2 == 0:
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        counter += 1
    else:
        pygame.draw.rect(screen, (255, 128, 0), player.rect)
        counter += 1
    pygame.display.flip()