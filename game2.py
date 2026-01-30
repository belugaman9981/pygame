import pygame
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("The Jumping Man")

x = 50
y = 50

width = 40
height = 60

velocity = 5


running = True
while running:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.
            
