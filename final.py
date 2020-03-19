"""An avoid the objects game."""

import pygame
from pygame.locals import *
import random
import time

# Setup
def intialize():
    """Loads necessary game aspects."""
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    score = 0
    Player = pygame.image.load("resources/images/player_character.png")
    Dungeon_Flooring = pygame.image.load("resources/images/dungeon_flooring.png")
    Coin = pygame.image.load("resources/images/coin.png")

def stopwatch(seconds):
    """Time based functions."""
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        score += 100
print("Get to the other side without being hit by the yellow blobs!")
def movement():
    """General position code"""
    keys = [False, False, False, False]
    Playerpos=[100,100]

    while 1:
        x = random.randint(0,640)
        y = random.randint(0,480)
        coinpos = [x,y]
        screen.blit(Coin,coinpos)

        if Playerpos == coinpos:
            Playerpos = [100,100]
        if Playerpos == [640,480]:
            print("Congrats! You did it!")
        pygame.display.flip()
        screen.fill(0)
        screen.blit(Player, Playerpos)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                score_board = open('Scores.txt', 'a')
                score_board.write(score)
                score_board.close()
                exit(0)
                #Movement
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=False
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False
        if keys[0]:
            Playerpos[1]-=0.1
        elif keys[2]:
            Playerpos[1]+=0.1
        if keys[1]:
            Playerpos[0]-=0.1
        elif keys[3]:
            Playerpos[0]+=0.1
def main():
    intialize()
    stopwatch(1000)
    movement()

if __name__ == "__main__":
    main()
    