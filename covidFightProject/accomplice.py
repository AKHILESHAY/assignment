from settings import *
import pygame
import math

class Accomplice:
    def __init__(self):
        self.x, self.y = player_pos
        self.perspective = player_previous_direction_horizon
        self.sensitivity = 0.004

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.keys_control()
        self.mouse_control()

    def keys_control(self):
        sin_a = math.sin(self.perspective)
        cos_a = math.cos(self.perspective)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.perspective -= 0.02
        if keys[pygame.K_RIGHT]:
            self.perspective += 0.02

    def mouse_control(self):
        if pygame.mouse.get_focused():
            angle_variation = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.perspective += angle_variation * self.sensitivity