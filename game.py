import pygame
import random
from utils import load_sprite
from model import GameObject

class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1200, 1080))
        self.background = load_sprite("ancient-pyramids", False)
        self.clock = pygame.time.Clock()
        cat = load_sprite("cat", True)
        self.bobs = []
        for i in range(0, 1000):
         self.bobs.append(GameObject((random.randint(-1600,1600),random.randint(-1000,1000)), cat, (random.randint(-15,15),random.randint(-15, 15))))
         

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Tapok")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        for b in self.bobs:
            b.move()
        
        
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        for b in self.bobs:
            b.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
