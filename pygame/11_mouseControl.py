#-*- coding: utf-8 -*-
from operator import truediv
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("마우스")
circleX_pos = 0
circleY_pos = 0

lk = pygame.mixer.Sound("pygame/source/lk.wav.wav")
rk = pygame.mixer.Sound("pygame/source/rk.wav.wav")

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            print("mouseMotion")
            print(pygame.mouse.get_pos())
            circleX_pos, circleY_pos = pygame.mouse.get_pos()
            screen.fill((11, 55, 26))
            pygame.draw.circle(screen, (255, 0, 255), (circleX_pos, circleY_pos), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouseMotion")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("l")
                lk.play()
            elif event.button == 3:
                print("r")
                rk.play()
            elif event.button == 2:
                print("hk")
            elif event.button == 4:
                print("hu")
            elif event.button == 5:
                print("hd")

        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseButtonup")
            pass
    pygame.display.update()
pygame.quit()
