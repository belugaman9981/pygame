import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("The Jumping Man")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False