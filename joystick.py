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
        if distanceBetweenCenters < borderDistance:
            return True
        return False


    def getCircleInsideBorder(self, mousePos: tuple[float]):
        p1, p2 = self.findSingleIntersects(mousePos)
        distance1 = globals.distanceMagnitude(p1, self.centre)
        distance2 = globals.distanceMagnitude(p2, self.centre)
        #return the point that is closest to the mouse 
        return p1 if distance1 > distance2 else p2


    def findSingleIntersects(self, mousePos: tuple[float]):
        """finds the two points where the a circle with radius self.mouseRadius 
        would intersect with the border circle just once"""
        px, py = mousePos
        cx, cy = self.centre
        #sol1 and sol2 are lambda values for the line function

        sol1top = (self.borderRadius - self.mouseRadius)**2 
        sol1bottom = (px - cx)**2 + (py - cy)**2
        assert sol1bottom != 0, "bottom of first solution should not be 0"

        sol2top = -1 * (self.borderRadius - self.mouseRadius)**2 
        sol2bottom = (px - cx)**2 + (py - cy)**2
        assert sol2bottom != 0, "bottom of second solution should not be 0"

        sol1 = sol1top/sol1bottom
        sol2 = sol2top/sol2bottom
        
        return self.line(sol1), self.line(sol2)

    def line(self, x):
        """returns the point on the line between the centre of the border
        circle and the mouse circle with lamdba value passed in"""
        return [
                self.centre[0] + (x * (self.currentCentre[0] - self.centre[0])),
                self.centre[1] + (x * (self.currentCentre[1] - self.centre[1]))
                ]
