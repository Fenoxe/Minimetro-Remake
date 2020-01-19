import pygame

class Route:

    def __init__(self, stations, circular, screen, color, startStation=0):
        self.stations = stations
        self.circular = circular
        self.currStationIndex = startStation
        self.direction = 1

        self.screen = screen
        self.color = color
        self.thickness = 3
    
    def getCurrentStation(self):
        return self.stations[self.currStationIndex]

    def getNextStation(self):
        self.currStationIndex += self.direction
        
        if self.currStationIndex == len(self.stations):
            if self.circular:
                self.currStationIndex = 0
            else:
                self.currStationIndex = len(self.stations) - 2
                self.direction = -1
        elif self.currStationIndex == -1:
            if self.circular:
                self.currStationIndex = len(self.stations) - 1
            else:
                self.currStationIndex = 1
                self.direction = 1
            
        return self.stations[self.currStationIndex]

    def copy(self):
        return Route(self.stations, self.circular)
    
    def draw(self):
        for i in range(1, len(self.stations)):
            pygame.draw.line(self.screen, self.color, self.stations[i-1].getPos(), self.stations[i].getPos(), self.thickness)
        if self.circular:
            pygame.draw.line(self.screen, self.color, self.stations[-1].getPos(), self.stations[0].getPos(), self.thickness)