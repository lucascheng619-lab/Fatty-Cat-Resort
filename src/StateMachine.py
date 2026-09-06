#Adapted from CS50's Introduction to Game Development course, by Colton Ogden

class StateMachine:
    def __init__(self, states):
        self.empty = type('EmptyState', (), {
            "enter": lambda params=None: None,
            "exit": lambda: None,
            "update": lambda params=None: None,
            "render": lambda params=None: None
        })

        self.states = states

        self.current_state = self.empty

    def change(self, state_name, enterParams=None):
        assert state_name in self.states, f"State {state_name} does not exist."
        self.current_state.exit()
        self.current_state = self.states[state_name]()
        self.current_state.enter(enterParams)

    def update(self, params = None):
        self.current_state.update(params)

    def render(self, params = None):
        self.current_state.render(params)