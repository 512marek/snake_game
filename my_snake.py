from time import sleep
import pygame
from pygame.locals import *
import sys
import random

def main():
    window_x, window_y = 600, 600

    pygame.init()

    WHITE = pygame.Color(255, 255, 255)
    GREEN = pygame.Color(0, 255, 0)
    TRANSPARENT = pygame.Color(0, 0, 0, 0)
    BLACK = pygame.Color(0,0,0)
    FPS = 10
    fpsClock = pygame.time.Clock()

    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("Snake")

    snake = [[300,300],
            [300, 280],
            [300, 260],
            [300, 240]]

    snake_width = 20
    speed_x = 0
    speed_y = 20
    direction = "DOWN"
    points = 0

    def draw_and_move_snake(snake, speed_x, speed_y):
        snake.pop()
        snake.insert(0, [snake[0][0] + speed_x, snake[0][1] + speed_y])
        for i in range(len(snake)):
            pygame.draw.rect(game_window, GREEN, snake[i] + [snake_width, snake_width])

    def key_pressed(direction, speed_x, speed_y):
        if event.key == K_DOWN and direction != "UP":
            direction = "DOWN"
            speed_x = 0
            speed_y = 20
        if event.key == K_UP and direction != "DOWN":
            direction = "UP"
            speed_x = 0
            speed_y = -20
        if event.key == K_LEFT and direction != "RIGHT":
            direction = "LEFT"
            speed_x = -20
            speed_y = 0
        if event.key == K_RIGHT and direction != "LEFT":
            direction = "RIGHT"
            speed_x = 20
            speed_y = 0
        return (speed_x, speed_y, direction)
        
    def generate_fruit():
        while True:
            flag = 1
            potential_fruit = [random.randint(0, (window_x-20)/20)*20, random.randint(0, (window_y-20)/20)*20]
            for part in snake:
                if part == potential_fruit:
                    flag = 0
            if flag:
                return potential_fruit

    def draw_fruit(fruit_position):
        pygame.draw.rect(game_window, WHITE, fruit_position + [snake_width, snake_width])

    def is_eaten():
        last = snake[len(snake) - 1]
        second = snake[len(snake) - 2]
        difference = [last[0] - second[0], last[1] - second[1]]  
        snake.append([last[0] - difference[0], last[1] - difference[1]])

    def is_dead():
        for part in snake:
            if part == snake[0] and part is not snake[0] or snake[0][0] == -20 or snake[0][0] == 600 or snake[0][1] == -20 or snake[0][1] == 600:
                
                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                textSurfaceObj = fontObj.render("You died, your score is: " + str(points), True, GREEN, TRANSPARENT)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (window_x/2, window_y/18)
                game_window.blit(textSurfaceObj, textRectObj)
                pygame.display.update()
                sleep(5)
                



                pygame.quit()
                sys.exit()

    fruit_position = generate_fruit()

    while True:
        flag = 1
        game_window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and flag == 1:
                speed_x, speed_y, direction = key_pressed(direction, speed_x, speed_y)
                flag = 0
        
        draw_and_move_snake(snake, speed_x, speed_y)
        if snake[0] == fruit_position:
            is_eaten()
            fruit_position = generate_fruit()
            points += 1
        
        draw_fruit(fruit_position)        
        is_dead()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()