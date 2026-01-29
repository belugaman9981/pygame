import pygame

pygame.init()

speed = int(input("Speed (1 to 10)? ")) * 6
direction = input("X, Y, or Both? ").lower()

x = 30
y = 30

if direction == "x":
    x = int(input("Where to start X level? "))
    
elif direction == "y":
    y = int(input("Where to start Y level? "))
    
elif direction == "both":
    x = int(input("Where to start X level? "))
    y = int(input("Where to start Y level? "))

screen = pygame.display.set_mode((640, 640))

potato_image = pygame.image.load("potato.png").convert_alpha()
potato_image = pygame.transform.scale(potato_image, (50, 50))


clock = pygame.time.Clock()
running = True
deltaT = .1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if direction == "x":
        x += 50 * deltaT
        
    elif direction == "y":
        y += 50 * deltaT
        
    elif direction == "both":
        x += 50 * deltaT
        y += 50 * deltaT

    screen.fill((0, 0, 0))
    screen.blit(potato_image, (x, y))
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
