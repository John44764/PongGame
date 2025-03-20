import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display_height = 500
display_width = 500
display = pygame.display.set_mode([display_width, display_height])

class Paddle1:
    width = 25
    height = 75
    x = 0
    y = display_height/2 - height / 2
    speed = 0.25


    def movePaddleY(amt):
        Paddle1.y = Paddle1.y + amt

paddle1 = Paddle1

class Paddle2:
    width = 25
    height = 75
    x = display_width - width
    y = display_height/2 - height / 2
    speed = 0.25

    def movePaddleY(amt):
        Paddle2.y = Paddle2.y + amt

paddle2 = Paddle2

class Ball:
    radius = 25
    X = display_width / 2
    Y = display_height / 2

    # top = Y - radius
    # bottom = Y + radius
    # left = X - radius
    # right = X + radius

    moveX = random.randint(-10, 10)
    moveY = random.randint(-10, 10)
    while moveX == 0:
        moveX = random.randint(-10, 10)

    def moveBall():
        Ball.X = Ball.X + Ball.moveX
        Ball.Y = Ball.Y + Ball.moveY

    counter = 1
    def moveBallAfter(frames):
        if Ball.counter % frames == 0:
            ball.moveBall()
        Ball.counter += 1

ball = Ball


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.key.get_pressed()[pygame.K_s] and paddle1.y <= display_height - paddle1.height:
        paddle1.movePaddleY(paddle1.speed)
    elif pygame.key.get_pressed()[pygame.K_w] and paddle1.y >= 0:
        paddle1.movePaddleY(-paddle1.speed)

    if pygame.key.get_pressed()[pygame.K_DOWN] and paddle2.y <= display_height - paddle2.height:
        paddle2.movePaddleY(paddle2.speed)
    elif pygame.key.get_pressed()[pygame.K_UP] and paddle2.y >= 0:
        paddle2.movePaddleY(-paddle2.speed)


    #                                       Rect(x, y, width, height)
    pygame.draw.rect(display, WHITE, pygame.Rect(paddle1.x, paddle1.y, paddle1.width, paddle1.height))

    #                                       Rect(x, y, width, height)
    pygame.draw.rect(display, WHITE, pygame.Rect(paddle2.x, paddle2.y, paddle2.width, paddle2.height))

    #
    pygame.draw.circle(display, WHITE, (ball.X, ball.Y), ball.radius)

    pygame.display.flip()
    display.fill(BLACK)

    if ball.Y - ball.radius <= 0:
        ball.moveY = -ball.moveY
    elif ball.Y + ball.radius >= display_height:
        ball.moveY = -ball.moveY

    # Check collision with Paddle 1
    if (
            ball.X - ball.radius <= paddle1.x + paddle1.width and
            paddle1.y <= ball.Y <= paddle1.y + paddle1.height
    ):
        ball.moveX = -ball.moveX

    # Check collision with Paddle 2
    if (
            ball.X + ball.radius >= paddle2.x and
            paddle2.y <= ball.Y <= paddle2.y + paddle2.height
    ):
        ball.moveX = -ball.moveX

    ball.moveBallAfter(75)#frames
