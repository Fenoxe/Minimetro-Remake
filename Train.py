import pygame
from Route import Route
from Station import Station

moveToCenterLeft = lambda t: (t[0] - 7, t[1] - 12)
train_icon = pygame.image.load("train.png")

class Train:

    def __init__(self, route, screen):
        self.capacity = 6
        self.riders = []
        self.route = route
        self.currentStation = route.getCurrentStation()
        self.pos = None
        self.updatePos()
        
        self.screen = screen
    
    def addRider(self, rider):
        assert len(self.capacity != 6)
        self.riders.append(rider)
    
    def contains(self, rider):
        if rider in self.riders:
            return True
        return False
    
    def getRider(self, rider):
        assert self.contains(rider)
        self.riders.remove(rider)
        return rider

    def updatePos(self):
        self.pos = self.currentStation.getPos()

    def moveToNextStation(self):
        self.currentStation = self.route.getNextStation()
        self.updatePos()

    def getPos(self):
        return self.pos

    def draw(self):
        self.screen.blit(train_icon, moveToCenterLeft(self.getPos()))