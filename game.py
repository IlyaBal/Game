import pygame
import random
from Apple import Apple
from utils import get_random_position, load_sprite, wrap_position
from model import GameObject
from Cat import Cat

class Game:
    
    def __init__(self):
        self._init_pygame()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("ancient-pyramids", False)
        self.clock = pygame.time.Clock()
        self.cat = Cat((400,300))
        self.apples = [Apple((get_random_position(self.screen))) for _ in range(6)]

       
         
    def _get_game_objects(self):
        return [*self.apples, self.cat]

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
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.cat.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.cat.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.cat.accelerate()
        if is_key_pressed[pygame.K_DOWN]:
            self.cat.accelerateback()
        if is_key_pressed[pygame.K_SPACE]:
            self.cat.Stop()
        if is_key_pressed[pygame.K_F1]:
            self.background = load_sprite("ancient-pyramids", False)

        if is_key_pressed[pygame.K_F2]:
            self.background = load_sprite("sky3", False)
        if is_key_pressed[pygame.K_F3]:
            self.background = load_sprite("sky2", False)
        

        if is_key_pressed[pygame.K_F5]:
            self.background = load_sprite("sky", False)
    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
