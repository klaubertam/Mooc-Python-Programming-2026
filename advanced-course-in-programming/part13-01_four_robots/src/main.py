import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
h=robot.get_height()
w=robot.get_width()

window.fill((0, 0, 0))
window.blit(robot, (0, 0))
window.blit(robot, (640-w, 0))
window.blit(robot, (0, 480-h))
window.blit(robot, (640-w, 480-h))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()