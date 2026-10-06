import pygame
import random
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

window.fill((0, 0, 0))
w=robot.get_width()
h=robot.get_height()
for i in range(1000):
    x = random.randint(0, 640 - w)
    y = random.randint(0, 480 - h)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()