import pygame, sys, random

HEIGHT = 640
WIDTH = 800
FPS = 15
fpsClock = pygame.time.Clock()
SIZE = 30
BLACK = (0, 0, 0)
GREN = (0, 255, 0)
RED = (255, 0, 0)
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
SPEED = 20
Display = pygame.display.set_mode((WIDTH, HEIGHT))

def finish():
    pygame.quit()
    sys.exit(0)

def make_new_appele():
    appale_x = random.randint(0, WIDTH - SIZE)
    appale_y = random.randint(0, HEIGHT - SIZE)
    appale = pygame.Rect(appale_x, appale_y, SIZE, SIZE)
    return appale

def add_part_of_snake(snake, snake_tail, head):
    update = [-SIZE * x for x in head]
    if len(snake_tail) == 0:
        snake_tail.append(snake.move(update[0], update[1]))
    else:
        snake_tail.append(snake_tail[len(snake_tail) - 1].move(update[0], update[1]))

def draw_snake(snake, snake_tail, head):
    tmp = snake.move(0, 0)
    speed_head = [SPEED * x for x in head]
    snake.move_ip(speed_head[0], speed_head[1])
    pygame.draw.rect(Display, GREN, snake)
    if len(snake_tail) == 0:
        return
    pygame.draw.rect(Display, (255, 255, 255), snake_tail[len(snake_tail) - 1])
    for i in range(0, len(snake_tail) - 1):
        snake_tail[len(snake_tail) - 1 - i] = snake_tail[len(snake_tail) - 2 - i]
        pygame.draw.rect(Display, GREN, snake_tail[len(snake_tail) - 1 - i])
    snake_tail[0] = tmp
    pygame.draw.rect(Display, GREN, snake_tail[0])

def main():
    snake = pygame.Rect(WIDTH / 2 - SIZE / 2, HEIGHT / 2 - SIZE / 2, SIZE, SIZE)
    head = RIGHT
    appale = make_new_appele()
    snake_tail = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and head != DOWN:
                    head = UP
                if event.key == pygame.K_DOWN and head != UP:
                    head = DOWN    
                if event.key == pygame.K_LEFT and head != RIGHT:
                    head = LEFT
                if event.key == pygame.K_RIGHT and head != LEFT:
                    head = RIGHT
        
        if snake.left < 0 or snake.right > WIDTH or snake.top < 0 or snake.bottom > HEIGHT:
            finish()
        if snake.colliderect(appale):
            appale = make_new_appele()
            add_part_of_snake(snake, snake_tail, head)
        Display.fill((255, 255, 255))
        
        pygame.draw.rect(Display, RED, appale)
        draw_snake(snake, snake_tail, head)
        pygame.display.update()
        fpsClock.tick(FPS)

main()