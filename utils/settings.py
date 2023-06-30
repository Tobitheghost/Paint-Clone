import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLACK = (42, 42, 42)
DARK_GRAY = (84, 84, 84)
GRAY = (126, 126, 126)
LIGHT_GRAY = (168, 168, 168)
RED = (255, 0, 0)
RED1 = (168, 0, 0)
RED2 = (126, 0, 0)
RED3 = (84, 0, 0)
RED4 = (42, 0, 0)
BLUE = (0, 255, 0)
BLUE1 = (0, 168, 0)
BLUE2 = (0, 126, 0)
BLUE3 = (0, 84, 0)
BLUE4 = (0, 42, 0)
GREEN = (0, 0, 255)
GREEN1 = (0, 0, 168)
GREEN2 = (0, 0, 126)
GREEN3 = (0, 0, 84)
GREEN4 = (0, 0, 42)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50


TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = (255, 255, 254)

DRAW_GRIDE_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)

