import pygame
from math import dist

pygame.init()

locations = {
    "HOME": (450, 500),
    "A": (150, 320),
    "B": (330, 130),
    "C": (620, 150),
    "D": (760, 330),
    "E": (650, 480),
    "F": (250, 500)
}

def distance(a, b):
    temp1, temp2 = 0, 0
    for loc in locations:
        if a == loc:
            temp1 = loc
        elif b == loc:
            temp2 = loc
    return dist(temp1, temp2)

def route_distance(route):
    total = 0
    for i in range(0, len(route)):
        total += distance(route[i], route[i+1])
    return total

route = ["HOME"]

clock = pygame.time.Clock()
gameloop = True
screen = pygame.display.set_mode()
time = 0

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        route = ["HOME"]

    clock.tick(30)
    if pygame.time.get_ticks() - time > 1000:
        time = pygame.time.get_ticks()
        print(f"Route: {route}")
    pygame.display.flip()

pygame.quit()