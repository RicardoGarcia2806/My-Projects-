#Created by: Ricardo Garcia 

#this script contains all the logic of the game 
import pygame
import sys 
import random
from Class import *

pygame.init()

SW, SH = 450, 450

BLOCK_SIZE = 50
FONT = pygame.font.Font(None, BLOCK_SIZE*2)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))

drawGrid()

snake = Snake()

apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()

    screen.fill('black')
    drawGrid()

    apple.update()

    score = FONT.render(f"{len(snake.body) + 1}", True, "white")

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    screen.blit(score, score_rect)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(10)