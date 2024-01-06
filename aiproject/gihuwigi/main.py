import pygame
import sys
import random
import time

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
player_size =  80
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5
player_image = pygame.image.load("aiproject/gihuwigi/image/ujs.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_size, player_size))
player_rect = player_image.get_rect(topleft=(player_x, player_y + player_size // 2))

# 이미지 크기 조절
player_image = pygame.transform.scale(player_image, (player_size, player_size))
player_rect = player_image.get_rect(topleft=(player_x, player_y))

# 적 설정
enemy_size = 50
enemy_images = [
    pygame.image.load("aiproject/gihuwigi/image/shs.png").convert_alpha(),
    pygame.image.load("aiproject/gihuwigi/image/ys.png").convert_alpha()
]
enemies = []
spawn_counter = 0

# 하트 설정
heart_image = pygame.image.load("heart.png")  # 하트 이미지 파일 경로에 따라 수정
heart_size = 30
hearts = 3


# 추가 변수
game_over = False
max_collisions = 3
collision_count = 0
invincible_duration = 1  # 초 단위
last_collision_time = 0

def spawn_enemy():
    try:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = -enemy_size
        enemy_speed = random.uniform(1, 5)
        enemy_image = random.choice(enemy_images)
        enemy_image_surface = enemy_image.convert_alpha() if enemy_image else None
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return

    if enemy_image_surface:
        # 이미지의 크기에서 일정 비율로 히트박스 크기 조절
        scale_factor = 0.8  # 예시로 80% 크기로 설정
        scaled_width = int(enemy_image_surface.get_width() * scale_factor)
        scaled_height = int(enemy_image_surface.get_height() * scale_factor)
        enemy_rect = pygame.Rect(
            enemy_x + (enemy_size - scaled_width) // 2,
            enemy_y + (enemy_size - scaled_height) // 2,
            scaled_width,
            scaled_height
        )
        enemies.append({
            "rect": enemy_rect,
            "speed": enemy_speed,
            "image": enemy_image_surface
        })

def draw_hearts():
    heart_spacing = 40
    for i in range(hearts):
        screen.blit(heart_image, (10 + i * heart_spacing, 10))

# 게임 루프
clock = pygame.time.Clock()

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if not game_over:
        # 이동
        if keys[pygame.K_a] and player_rect.x > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_d] and player_rect.x < width - player_rect.width:
            player_rect.x += player_speed
        if keys[pygame.K_w] and player_rect.y > 0:
            player_rect.y -= player_speed
        if keys[pygame.K_s] and player_rect.y < height - player_rect.height:
            player_rect.y += player_speed

        # 플레이어와 적 충돌 체크
        for enemy in enemies:
            if player_rect.colliderect(enemy["rect"]):
                if time.time() - last_collision_time > invincible_duration:
                    last_collision_time = time.time()
                    # 충돌 횟수 증가
                    collision_count += 1
                    print(f"Collision Count: {collision_count}")

                    if collision_count >= max_collisions:
                        print("Game Over!")
                        game_over = True
                    else:
                        # 무적 상태일 때 반투명 처리
                        player_image.set_alpha(128)  # 0(투명)에서 255(불투명) 사이의 값 설정
                        pygame.time.set_timer(pygame.USEREVENT, int(invincible_duration * 1000))  # 타이머 설정

    
        # 플레이어 그리기
        screen.blit(player_image, player_rect.topleft)

        # 충돌 감지 및 처리
        for enemy in enemies:
            if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(enemy["rect"]):
                # 충돌 시 하트 감소
                hearts -= 1
                if hearts == 0:
                    running = False  # 게임 오버
                else:
                    # 하트가 남아있으면 적 다시 생성
                    enemy["rect"].y = -enemy_size
                    enemy["rect"].x = random.randint(0, width - enemy_size)

        # 하트 그리기
        draw_hearts()

        # 적 생성
        spawn_counter += 1
        if spawn_counter >= 60:
           spawn_enemy()
           spawn_counter = 0

        # 이동하는 적
        for enemy in enemies:
            enemy["rect"].y += enemy["speed"]

        # 배경 그리기
        screen.blit(background_image, background_rect)

        # 적 그리기
        for enemy in enemies:
            if enemy["image"]:
                screen.blit(enemy["image"], enemy["rect"].topleft)


    pygame.display.flip()

    # 초당 프레임 수
    clock.tick(60)

        # 무적 상태 해제
    if game_over or (time.time() - last_collision_time > invincible_duration and player_image.get_alpha() != 255):
        player_image.set_alpha(255)
        pygame.time.set_timer(pygame.USEREVENT, 0)  # 타이머 해제