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
mouse_down_pos = (0, 0)

clock = pygame.time.Clock()
gameloop = True
screen = pygame.display.set_mode()
time = 0

while gameloop:
    print(route)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down_pos = event.pos
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        route = ["HOME"]

    for place in locations:
        val = locations[place]
        location_rect = pygame.Rect(val[0], val[1], 50, 50)
        pygame.draw.rect(screen, (255, 255, 255), location_rect)
        if location_rect.collidepoint(mouse_down_pos[0], mouse_down_pos[1]) and place not in route:
            route.append(place)

    clock.tick(30)
    if pygame.time.get_ticks() - time > 1000:
        time = pygame.time.get_ticks()
        print(f"Route: {route}")
    pygame.display.flip()

pygame.quit()