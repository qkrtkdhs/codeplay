#-*- coding: utf-8 -*-
from operator import truediv
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("컨닝왕")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if guege <= 50000:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score += 1
                    print(score)
        else:
            guege = 0
            score = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                score = 0
                print(score)

pygame.quit()
