from src.StateMachine import StateMachine
from src.states.BaseState import BaseState

gStateMachine = StateMachine({
    'BaseState': lambda: BaseState()
})