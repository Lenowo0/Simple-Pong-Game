import pygame, sys, random

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('lol')

bg_color = pygame.Color('white')

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 12,120)
opponent = pygame.Rect(10, screen_height / 2 - 70, 12,120)

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7                
                

    ball_movements()
    player_movements()
    opponent_movements()

    screen.fill(bg_color)
    pygame.draw.rect(screen, "black", player)
    pygame.draw.rect(screen, "black", opponent)
    pygame.draw.ellipse(screen, "black", ball)

    pygame.display.flip()
    clock.tick(60)        