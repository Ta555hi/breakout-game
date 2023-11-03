import pygame
from random import randrange as rnd
pygame.init()
from pygame import mixer
mixer.init()


WIDTH, HEIGHT = 600, 400
fps = 60

sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Block Breaker Game')
clock = pygame.time.Clock()
text = pygame.font.Font(None, 40)

#background image
background = pygame.image.load("blue space.jpg").convert()

#paddle setting
paddle_w = 75
paddle_h = 10
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
dx, dy = 1, -1

#ball settings
ball_radius = 12
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# block settings
block_list = [pygame.Rect(10 + 120 * i, 10 + 50 * j, 100, 35) for i in range (5) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range (10) for j in range(5)]

mixer.music.load('Extreme-Sport-Trap-Music-PISTA(chosic.com).mp3')
mixer.music.play()

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dy
    return dx, dy

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(background, (0, 0))
   
    #drawing world
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(sc, pygame.Color('darkorange'), paddle)
    pygame.draw.circle(sc, (255, 255, 255), ball.center, ball_radius)

    #ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # collision left right
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    # collision top
    if ball.centery < ball_radius:
        dy = -dy

    #collision paddle
    if ball.colliderect(paddle) and dy > 0:
        dy, dy = detect_collision(dx, dy, ball, paddle)

    # collision blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)

        #special effect
        hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
        pygame.draw.rect(sc, hit_color, hit_rect)
        fps ** 2
    
    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    # game over
    game_over = False
    
     # game over
    if ball.bottom > HEIGHT:
        game_over_text = text.render('GAME OVER!', True, (255, 0 ,0 ))  
        # replay_text = text.render('Press K to replay', True, (255, 0 ,0 ))
        sc.blit(game_over_text, (200, 250))
        # sc.blit(replay_text, (200, 300))
    elif not len(block_list):
        win_text = text.render('YOU WON!!!', True, (255, 215, 0))
        sc.blit(win_text, (200, 250))

    #update screen
    pygame.display.flip()
    clock.tick(fps)
    
    