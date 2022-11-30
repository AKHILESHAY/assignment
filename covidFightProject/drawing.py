import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'a': pygame.image.load('img/wp06.png').convert(),
                         'b': pygame.image.load('img/wp07.png').convert(),
                         'c': pygame.image.load('img/wp05.png').convert(),
                         'd': pygame.image.load('img/wp08.png').convert(),
                         'e': pygame.image.load('img/wp03.png').convert(),
                         'm': pygame.image.load('img/C01.png').convert()
                         }

    def background(self, view):
        sky_offset = -5 * math.degrees(view) % WIDTH
        self.sc.blit(self.textures['m'], (sky_offset, 0))
        self.sc.blit(self.textures['m'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['m'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_previous_direction_horizon):
        ray_casting(self.sc, player_pos, player_previous_direction_horizon, self.textures)
 
    def display_storyline_with_payoffs(self, text, x, y):
        indicator_num = 0
        display_text1 = "  "
        render1 = self.font.render(display_text1, 0, WHITE)
        value1 = int(x)
        value2 = int(y)

        if value1 >= 1003:
            if value2 >= 117:
                if value2 <= 205:
                    indicator_num = 1
                    display_text1 = "You got vaccinated."
                    render1 = self.font.render(display_text1, 0, SANDY)
        elif value2 >= 600:
            if value1 >= 126:
                if value1 <= 204:
                    indicator_num = 2
                    display_text1 = "You got infected with Covid virus."
                    render1 = self.font.render(display_text1, 0, BLUE)
        else:
            display_text1 = text
            render1 = self.font.render(display_text1, 0, WHITE)
         
        self.sc.blit(render1, TEXT_POS)
        self.payoff_accomplice(indicator_num)
        
    def payoff_accomplice(self, indicator_num):
        display_text1 = "  "
        display_text2 = "  "
        payoff_render1 = self.font.render(display_text1, 0, WHITE)
        payoff_render2 = self.font.render(display_text2, 0, WHITE)
        if indicator_num == 1:
            display_text1 = "PAY OFF 1: " 
            display_text2 = "PAY OFF 2: "
            payoff_render1 = self.font.render(display_text1, 0, WHITE)
            payoff_render2 = self.font.render(display_text2, 0, WHITE)
        elif indicator_num == 2:
            display_text1 = "PAY OFF 1: "
            display_text2 = "PAY OFF 2: "
            payoff_render1 = self.font.render(display_text1, 0, WHITE)
            payoff_render2 = self.font.render(display_text2, 0, WHITE)
            
        self.sc.blit(payoff_render1, TEXT_POS2)
        self.sc.blit(payoff_render2, TEXT_POS3)

    def mini_map(self, accomplice):
        self.sc_map.fill(BLACK)
        map_x, map_y = accomplice.x // MAP_SCALE, accomplice.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(accomplice.perspective),
                                                 map_y + 12 * math.sin(accomplice.perspective)), 2)
        pygame.draw.circle(self.sc_map, BLUE, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, RED, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
      
        
        
        
        
        
 