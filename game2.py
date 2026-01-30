import pygame
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = "The Jumping Man"
window.borderless = False
window.exit_button._visible = True
window.fps_counter.enabled  = True

Sky(color= color.cyan)

player = FirstPersonController(
    y=2,
    speed=6,
    jump_height=1.5
)