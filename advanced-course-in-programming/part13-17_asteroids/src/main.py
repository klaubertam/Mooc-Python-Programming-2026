# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
w = robot.get_width()
h = robot.get_height()

x = 0
y = 0

speed = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Move right
    if y == 0 and x < 640 - w:
        x += speed

    # Move down
    elif x >= 640 - w and y < 480 - h:
        y += speed

    # Move left
    elif y >= 480 - h and x > 0:
        x -= speed

    # Move up
    elif x == 0 and y > 0:
        y -= speed

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))

    pygame.display.flip()
    clock.tick(60)