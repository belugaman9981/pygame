import pygame

pygame.init()

user_input_speed = int(int(input("Speed (1 to 10)? "))) * 6

user_input_cords = input()

screen = pygame.display.set_mode((640, 640))

potato_image = pygame.image.load("potato.png").convert_alpha()

new_width  = 50
new_height = 50

potato_image = pygame.transform.scale(potato_image, (new_width, new_height))

running = True
x = 30
clock = pygame.time.Clock()

deltaT = .1

while running:
    
    screen.blit(potato_image, (x, 100))
    
    x += 50 * deltaT
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
    clock.tick(user_input_speed)


pygame.quit()

