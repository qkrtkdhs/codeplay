import pygame
import sys
import random
import math

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SSG")

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 배경 설정
background_image = pygame.image.load("aiproject/gihuwigi/image/bg.jpg").convert()
background_rect = background_image.get_rect()

# 플레이어 설정
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
player_image = pygame.image.load("aiproject/gihuwigi/image/ujs.png").convert_alpha()
player = {"rect": player_rect, "image": player_image, "speed": player_speed}

# 적 설정
enemy_size = 50
enemy_speed = 2
enemy_images = [
    "aiproject/gihuwigi/image/ys.png",  # 적 이미지 파일 경로 1
    "aiproject/gihuwigi/image/shs.png"  # 적 이미지 파일 경로 2
]
enemies = []

def spawn_enemy():
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = -enemy_size
    enemy_image = pygame.image.load(random.choice(enemy_images)).convert_alpha()
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    enemies.append({"rect": enemy_rect, "image": enemy_image, "speed": enemy_speed})

def is_collision(obj1, obj2):
    obj1_rect = obj1["rect"]
    obj2_rect = obj2["rect"]

    return obj1_rect.colliderect(obj2_rect)

# 게임 루프
clock = pygame.time.Clock()

bullet_cooldown = 0  # 총알 쿨다운 초기화

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # 이동
    if keys[pygame.K_a] and player["rect"].x > 0:
        player["rect"].x -= player["speed"]
    if keys[pygame.K_d] and player["rect"].x < width - player["rect"].width:
        player["rect"].x += player["speed"]
    if keys[pygame.K_w] and player["rect"].y > 0:
        player["rect"].y -= player["speed"]
    if keys[pygame.K_s] and player["rect"].y < height - player["rect"].height:
        player["rect"].y += player["speed"]

    # 적 생성
    if random.randint(0, 100) < 2:
        spawn_enemy()

    # 이동하는 적
    for enemy in enemies:
        enemy["rect"].y += enemy["speed"]

    # 배경 그리기
    screen.blit(background_image, background_rect)

    # 플레이어 그리기
    screen.blit(player["image"], (player["rect"].x, player["rect"].y))

    # 적 그리기
    for enemy in enemies:
        screen.blit(enemy["image"], (enemy["rect"].x, enemy["rect"].y))

    pygame.display.flip()

    # 초당 프레임 수
    clock.tick(60)