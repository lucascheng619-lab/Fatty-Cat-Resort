import pygame
from src.Globals import *

#imports all the constants from the constants.py file
from src.constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))

clock = pygame.time.Clock()

#Toggles fullscreen
pygame.display.toggle_fullscreen()

running = True

while running:
    events = pygame.event.get()
    dt = clock.tick()

    for event in events:
        #if the 'X' button at the top of the button is pressed the game will stop
        if event.type == pygame.QUIT:
            running = False

        

    gStateMachine.update({
        "dt":dt, #delta time is the used to scale movements
        "events":events #get events because this can only be triggered once every update
    })

    gStateMachine.render({
        "canvas":canvas
    })

    #makes scaled canvas is the canvas that is scaled to the size of the screen so that it can still look big on screen

    scaled_canvas = pygame.transform.scale(canvas, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #put scaled canvas on the screen

    screen.blit(scaled_canvas, (0, 0))


    #updates the screen
    #ESSENTIAL
    pygame.display.update() 


    
