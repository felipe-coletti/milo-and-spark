import pygame
from graphics import spritesheet

class CharacterSkin:
    BORDER = 3
    SPACING = 3
    COLUMN_WIDTH = 23

    def __init__(self, path, scale = 2):
        self.scale = scale

        image = pygame.image.load(path).convert_alpha()
        sheet = spritesheet.Spritesheet(image)

        self.frames = self._load_frames(sheet)

    def _sprite(self, sheet, x, y):
        return sheet.get_image(
            0,
            x,
            y,
            23,
            57,
            self.scale,
            (0, 0, 0)
        )

    def _load_frames(self, sheet):
        down_0 = self._sprite(
            sheet,
            3,
            3
        )
        down_1 = self._sprite(
            sheet,
            29,
            3
        )
        down_2 = self._sprite(
            sheet,
            55,
            3
        )
        up_0 = self._sprite(
            sheet,
            3,
            61
        )
        up_1 = self._sprite(
            sheet,
            29,
            61
        )
        up_2 = self._sprite(
            sheet,
            55,
            61
        )
        right_0 = self._sprite(
            sheet,
            3,
            123
        )
        right_1 = self._sprite(
            sheet,
            29,
            123
        )
        right_2 = self._sprite(
            sheet,
            55,
            123
        )
        left_0 = self._sprite(
            sheet,
            3,
            183
        )
        left_1 = self._sprite(
            sheet,
            29,
            183
        )
        left_2 = self._sprite(
            sheet,
            55,
            183
        )

        return {
            "down": [down_0, down_1, down_0, down_2, down_0],
            "left": [left_0, left_1, left_0, left_2, left_0],
            "right": [right_0, right_1, right_0, right_2, right_0],
            "up": [up_0, up_1, up_0, up_2, up_0],
        }
