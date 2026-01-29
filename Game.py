import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

potato_image = pygame.image.load("potato.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

