import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
FPS = 15

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
        
    def move(self):
        if self.direction == "RIGHT":
            self.x += CELL_SIZE
        elif self.direction == "LEFT":
            self.x -= CELL_SIZE
        elif self.direction == "UP":
            self.y -= CELL_SIZE
        elif self.direction == "DOWN":
            self.y += CELL_SIZE
            
        self.body.insert(0, (self.x, self.y))
        
    def grow(self):
        self.body = self.body[:-1]
        
    def check_collision(self):
        # Столкновение со стенами
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return True
        # Столкновение с собой
        if (self.x, self.y) in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = self.random_position()
        
    def random_position(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return (x, y)
    
    def respawn(self):
        self.position = self.random_position()

def main():
    snake = Snake()
    food = Food()
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
        
        # Движение змейки
        snake.move()
        
        # Проверка столкновений
        if snake.check_collision():
            pygame.quit()
            sys.exit()
            
        # Проверка поедания еды
        if (snake.x, snake.y) == food.position:
            score += 1
            food.respawn()
        else:
            snake.grow()
        
        # Отрисовка
        screen.fill(BLACK)
        
        # Отрисовка еды
        pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))
        
        # Отрисовка змейки
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        
        # Обновление экрана
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()