import pygame
from Station import Station
from Route import Route
from Train import Train

def render(stations, routes, trains):
    screen.blit(bg_image, (0,0))
    for station in stations:
        station.draw()

    for route in routes:
        route.draw()

    for train in trains:
        train.draw()
    pygame.display.flip()

def setup(numStations, numTrains, screen):
    stations = []
    t_pos = [
        (100, 400),
        (300, 100),
        (600, 200),
        (800, 500),
        (900, 200),
        (400, 900),
    ]
    for i in range(numStations):
        stations.append(Station(t_pos[i], screen))

    routes = []
    t_stations = [
        [0, 1, 2, 3],
        [1, 2, 4, 5]
    ]
    t_circular = [
        True,
        False
    ]
    t_colors = [
        (0, 0, 255),
        (255, 0, 0)
    ]
    for i in range(numRoutes:=2):
        s = [stations[x] for x in t_stations[i]]
        routes.append(Route(s, t_circular[i], screen, t_colors[i]))
    
    trains = []
    for i in range(numTrains):
        trains.append(Train(routes[i], screen))
    
    return stations, routes, trains

pygame.init()

bg_image = pygame.image.load("bg.png")

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("minimetro")
screen.blit(bg_image, (0,0))

stations, routes, trains = setup(6, 2, screen)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            for train in trains:
                train.moveToNextStation()
    
    render(stations, routes, trains)

pygame.display.quit()
pygame.quit()
exit()