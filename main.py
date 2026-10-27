import pygame

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