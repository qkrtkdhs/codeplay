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
background_image = pygame.image.load("aiproject/gihuwigi/image/bg.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))
background_rect = background_image.get_rect()
background_y = 0  # 배경의 y 좌표

# 플레이어 설정
player_size = 80
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5
player_image = pygame.image.load("aiproject/gihuwigi/image/ujs.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# 이미지 크기 조절
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# 플레이어 히트박스 크기 조절
player_hitbox_scale = 0.8  # 히트박스 크기 비율 조절
scaled_player_width = int(player_size * player_hitbox_scale)
scaled_player_height = int(player_size * player_hitbox_scale)

player_rect = pygame.Rect(
    player_x + (player_size - scaled_player_width) // 2,
    player_y + (player_size - scaled_player_height) // 2,
    scaled_player_width,
    scaled_player_height
)

# 적 설정
enemy_size = 50
enemy_images = [
    pygame.image.load("aiproject/gihuwigi/image/shs.png").convert_alpha(),
    pygame.image.load("aiproject/gihuwigi/image/ys.png").convert_alpha()
]
enemies = []
spawn_counter = 0
enemy_speed_increment = 1

# 하트 설정
heart_image = pygame.image.load("aiproject/gihuwigi/image/hrt.png")  # 하트 이미지 파일 경로에 따라 수정
heart_size = 50
hearts = 3


# 추가 변수
game_over = False
max_collisions = 3
collision_count = 0
invincible_duration = 1
last_collision_time = 0
score = 0
story_displayed = False  # 스토리가 이미 표시되었는지 여부를 나타내는 변수
game_started = False  # 게임이 시작되었는지 여부를 나타내는 변수

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
        scale_factor = 0.6
        scaled_width = int(enemy_image_surface.get_width() * scale_factor)
        scaled_height = int(enemy_image_surface.get_height() * scale_factor)

        # 히트박스를 오른쪽으로 옮김
        enemy_rect = pygame.Rect(
            enemy_x + (enemy_size - scaled_width) // 2 + 10,  # 여기서 10은 조절할 값입니다
            enemy_y + (enemy_size - scaled_height) // 2,
            scaled_width,
            scaled_height
        )
        enemies.append({
            "rect": enemy_rect,
            "speed": enemy_speed,
            "image": enemy_image_surface
        })
        enemy_speed += enemy_speed_increment

def draw_hearts():
    heart_spacing = 20  # 하트 간격을 조절할 수 있습니다.
    for i in range(hearts):
        heart_rect = heart_image.get_rect(topleft=(10 + i * (heart_size + heart_spacing), 10))
        heart_surface = pygame.transform.scale(heart_image, (heart_size, heart_size))
        
        # Draw hearts only up to the remaining lives
        if i < (hearts - collision_count):
            screen.blit(heart_surface, heart_rect)

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if not game_started and event.key == pygame.K_RETURN:
                game_started = True
                story_displayed = True  # 스토리 표시 완료
                spawn_enemy()  # 게임 시작 시 적을 생성

    if game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if not game_over:
            score += clock.get_time() / 100
            # 이동
            if keys[pygame.K_LEFT] and player_rect.x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_rect.x < width - player_size:
                player_x += player_speed
            if keys[pygame.K_UP] and player_rect.y > 0:
                player_y -= player_speed
            if keys[pygame.K_DOWN] and player_rect.y < height - player_size:
                player_y += player_speed

            # 플레이어 히트박스 업데이트
            player_rect.topleft = (
                player_x + (player_size - scaled_player_width) // 2,
                player_y + (player_size - scaled_player_height) // 2
            )

            # 배경 스크롤
            background_y += 5  # 스크롤 속도를 조절할 수 있습니다.
            if background_y >= height:
                background_y = 0

            # 배경 그리기
            screen.blit(background_image, (0, background_y - height))
            screen.blit(background_image, (0, background_y))

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

            # 하트 그리기
            draw_hearts()

            # 적 생성
            spawn_counter += 1.5
            if spawn_counter >= 60:
                spawn_enemy()
            spawn_counter = 0

            # 이동하는 적
            for enemy in enemies:
                enemy["rect"].y += enemy["speed"]

            # 적 그리기
            for enemy in enemies:
                if enemy["image"]:
                    screen.blit(enemy["image"], enemy["rect"].topleft)

        # 초당 프레임 수
        clock.tick(60)

            # 무적 상태 해제
        if game_over or (time.time() - last_collision_time > invincible_duration and player_image.get_alpha() != 255):
            player_image.set_alpha(255)
            pygame.time.set_timer(pygame.USEREVENT, 0)

        if game_over:
            font_size = 80  # 원하는 폰트 크기로 조절
            font = pygame.font.Font(None, font_size)

            # 게임 오버와 점수를 나누어 각각 렌더링
            game_over_text = font.render("Game over!", True, white)
            score_text = font.render(f"Score: {int(score)}", True, white)

            # 텍스트의 rect를 가져와 위치를 조절하여 화면에 표시
            game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2 - font_size // 2))
            score_rect = score_text.get_rect(center=(width // 2, height // 2 + font_size // 2))

            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)
        else:
            font_size = 60  # 원하는 폰트 크기로 조절
            font = pygame.font.Font(None, font_size)
            score_text = font.render(f"Score: {int(score)}", True, white)
            score_rect = score_text.get_rect(topleft=(width - 10 - score_text.get_width(), 10))  # 화면 오른쪽 위로 조절

            screen.blit(score_text, score_rect)

        pygame.display.flip()

    else:
        # 게임이 시작되지 않은 경우에는 스토리를 표시
        if not story_displayed:
            screen.fill(black)  # 화면을 검은색으로 채움
            font = pygame.font.Font(None, 36)
            story_text = font.render("옛날 옛적에...", True, white)
            story_rect = story_text.get_rect(center=(width // 2, height // 2))
            screen.blit(story_text, story_rect)

            # 엔터를 누르면 스토리 표시 완료
            keys = pygame.key.get_pressed()  # 여기로 이동
            if keys[pygame.K_RETURN]:
                story_displayed = True

        # 스토리가 표시된 후에는 "Enter 키를 눌러 시작" 표시
        else:
            screen.fill(black)
            font = pygame.font.Font(None, 36)
            start_text = font.render("Enter 키를 눌러 시작", True, white)
            start_rect = start_text.get_rect(center=(width // 2, height // 2))
            screen.blit(start_text, start_rect)

    pygame.display.flip()

    clock.tick(60)