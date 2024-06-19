import pygame
import random

# 초기화
pygame.init()

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블럭깨기 게임")

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_speed = 6
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)

# 공 설정
ball_radius = 10
ball_speed = [4, -4]
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

# 블록 설정
block_width = 75
block_height = 30
blocks = []
for x in range(10):
    for y in range(5):
        blocks.append(pygame.Rect(x * (block_width + 10) + 35, y * (block_height + 10) + 50, block_width, block_height))

# 폰트 설정
font = pygame.font.SysFont(None, 36)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.move_ip(paddle_speed, 0)

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽과의 충돌 처리
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        running = False  # 게임 오버

    # 패들과의 충돌 처리
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블록과의 충돌 처리
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)
    
    if not blocks:
        text = font.render("YOU WIN!", True, WHITE)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
