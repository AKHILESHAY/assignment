import pygame
from settings import *
from accomplice import Accomplice
import math
from map import world_map
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
accomplice = Accomplice()
drawing = Drawing(sc, sc_map)
text = "Storyline: You are to fight Covid by getting vaccinated."


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    accomplice.movement()
    sc.fill(BLACK)

    drawing.background(accomplice.perspective)
    drawing.world(accomplice.pos, accomplice.perspective)
    drawing.display_storyline_with_payoffs(text, accomplice.x, accomplice.y)
    drawing.mini_map(accomplice)

    pygame.display.flip()
    clock.tick()