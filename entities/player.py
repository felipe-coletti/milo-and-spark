import pygame
from entities.character import Character

class Player(Character):
    def __init__(self, skin, position):
        super().__init__(skin, position)

    def update(self, keys, screen):
        moving = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = "left"
            self.rect.x = max(self.rect.x - self.speed, 0)
            moving = True

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "right"
            self.rect.x = min(
                self.rect.x + self.speed,
                screen.get_width() - self.rect.width
            )
            moving = True

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = "up"
            self.rect.y = max(self.rect.y - self.speed, 0)
            moving = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "down"
            self.rect.y = min(
                self.rect.y + self.speed,
                screen.get_height() - self.rect.height
            )
            moving = True

        self.animate(moving)
