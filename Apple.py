from model import GameObject
from utils import get_random_velocity, load_sprite


class Apple(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("pomodoro"), get_random_velocity(1, 3))
        