from gymnasium import Env
from pyboy import PyBoy

class GoldGymEnv(Env, config):
    def __init__(self):
        self.valid_actions = [
            WindowEvent.PRESS_ARROW_DOWN,
            WindowEvent.PRESS_ARROW_UP,
            WindowEvent.PRESS_ARROW_RIGHT,
            WindowEvent.PRESS_ARROW_LEFT,
            WindowEvent.PRESS_BUTTON_A,
            WindowEvent.PRESS_BUTTON_B
        ]
        self.action_space = spaces