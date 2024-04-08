from pygame.math import Vector2
from model import UP, GameObject
from utils import load_sprite
from pygame.transform import rotozoom

class Cat(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25

    def __init__(self, position):
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("cat"), Vector2(0))
        
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
        
    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
        
    def accelerateback(self):
        self.velocity -= self.direction * self.ACCELERATION
        
    def Stop(self):
        self.velocity = (0,0)