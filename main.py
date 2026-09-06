import pygame
from src.Globals import *

#imports all the constants from the constants.py file
from src.constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


gStateMachine.change('BaseState')

gStateMachine.update()