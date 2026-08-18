import pygame
import os

from graphics.character_skin import CharacterSkin
from entities.player import Player

class Game:
    def __init__(self):
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Milo & Spark")

        self.clock = pygame.time.Clock()
        self.running = True

        self.sky_color = (163, 212, 255)

        skin = CharacterSkin(
            os.path.join(
                "assets",
                "images",
                "characters",
                "milo",
                "milo.png"
            )
        )

        self.player = Player(skin, (150, 150))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.screen)

    def draw(self):
        self.screen.fill(self.sky_color)

        self.player.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(60)