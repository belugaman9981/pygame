import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

potato_image = pygame.image.load("potato.png").convert()

running = True
x = 30
clock = pygame.time.Clock()

deltaT = .1

while running:
    
    screen.blit(potato_image, (x, 30))
    
    x += 50 * deltaT
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
    clock.tick(60)


pygame.quit()

