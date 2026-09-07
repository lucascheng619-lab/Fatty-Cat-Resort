import pygame
#import stateMachine + states
from src.StateMachine import StateMachine
from src.states.BaseState import BaseState
from src.states.game.PlayState import PlayState

gStateMachine = StateMachine({
    "BaseState": lambda: BaseState(),
    "PlayState": lambda: PlayState()
})
