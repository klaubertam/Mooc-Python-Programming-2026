import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

window.fill((0, 0, 0))
w=robot.get_width()

for i in range(10):
    for j in range(10):
        window.blit(robot, (i*w+50+j, j*10+100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()