import pygame
from collections import deque

station_icon = pygame.image.load("station.png")
centerToLeft = lambda t: (t[0] - 25, t[1] - 25)

class Station:

    def __init__(self, pos, screen):
        self.riders = deque()
        self.pos = pos
        
        self.screen = screen
    
    def addRider(self, rider):
        self.riders.append(rider)
    
    def getRider(self):
        return self.riders.popleft()

    def getPos(self):
        return self.pos
        
    def draw(self):
        self.screen.blit(station_icon, centerToLeft(self.getPos()))