import pygame

class Character:
    def __init__(self, skin, position, speed=5):
        self.skin = skin

        self.rect = pygame.Rect(
            position[0],
            position[1],
            69,
            171
        )

        self.direction = "down"

        self.speed = speed

        self.frame_index = 0
        self.animation_speed = speed / 50

    def animate(self, moving):
        if moving:
            self.frame_index += self.animation_speed

            if self.frame_index >= len(
                    self.skin.frames[self.direction]
            ):
                self.frame_index = 0
        else:
            self.frame_index = 0

    def draw(self, screen):
        frame = int(self.frame_index)

        char = self.skin.frames[self.direction][frame]

        screen.blit(char, self.rect)