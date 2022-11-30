import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
#FPS = 60
TILE = 100
TEXT_POS = (WIDTH - 1025, 5)
TEXT_POS2 = (WIDTH - 1025, 40)
TEXT_POS3 = (WIDTH - 1025, 80)

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player settings
initial_position_height = HALF_HEIGHT - 220
initial_position_width = HALF_WIDTH - 360
player_pos = (initial_position_width, initial_position_height)
player_previous_direction_horizon = -3.15
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)

