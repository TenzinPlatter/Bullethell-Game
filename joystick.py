import pygame
import math
import globals


class Joystick:
    def __init__(self, centre: tuple):
        self.centre = centre
        self.currentCentre = (0, 0)
        self.mouseRadius = 10
        self.borderRadius = 120

        
    def draw(self, window):
        """Need to call joystick draw first as it will put down a full circle
        then a smaller circle on top to make an outline, if called later will
        possibly cover other assets"""
        mousePos = pygame.mouse.get_pos()
        #draw border
        pygame.draw.circle(window, center = self.centre, color = (0, 0, 0), radius = self.borderRadius)
        #same fill as background
        pygame.draw.circle(window, center = self.centre, color = (105, 105, 105), radius = self.borderRadius - 5)
        pygame.draw.circle(window, center = self.currentCentre, color = (255, 255, 255), radius = self.mouseRadius)


    def setCentre(self):
        """sets the joysticks current point, needs to be called in game loop
        before player events"""
        mousePos = pygame.mouse.get_pos()
        if self.insideBorder(mousePos):
            self.currentCentre = mousePos
        else:
            self.currentCentre = self.getCircleInsideBorder(mousePos)
            
    def getMoveVector(self):
        """
        returns the unit vector for the joysticks current direction
        from its centre
        """
        dx = self.currentCentre[0] - self.centre[0]
        dy = self.currentCentre[1] - self.centre[1]
        magnitude = globals.distanceMagnitude(self.currentCentre, self.centre)
        if magnitude == 0:
            return 0, 0
        unitVec = [dx/magnitude, dy/magnitude]
        return unitVec

    def insideBorder(self, mousePos: tuple[float]):
        """will check if a circle at the mousePos passed is inside the border
        circle, returns boolean"""
        distanceBetweenCenters = globals.distanceMagnitude(mousePos, self.centre)
        borderDistance = self.borderRadius - self.mouseRadius
        return distanceBetweenCenters < borderDistance


    def getCircleInsideBorder(self, mousePos: tuple[float]):
        # check page 7 in programming book for explanation
        dirVector = [
                mousePos[0] - self.centre[0],
                mousePos[1] - self.centre[1]
                ]
        k = (self.borderRadius - self.mouseRadius) / globals.distanceMagnitude(self.centre, mousePos)
        point = [
                self.centre[0] + k * dirVector[0],
                self.centre[1] + k * dirVector[1]
                ]
        return point
