class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint):
        # The following 0 assignments are placeholders
        # to make the coe run. They need to be made to
        # calculate the coordinates of the new midpoint.
        newX = (self.xCoord + otherPoint.xCoord)/2
        newY = (self.yCoord + otherPoint.yCoord)/2
        return Point(newX, newY)
