class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        closeX = -1
        closeY = -1
        if xCenter < x1:
            closeX = x1
        elif xCenter > x2:
            closeX = x2
        else:
            closeX = xCenter

        if yCenter < y1:
            closeY = y1
        elif yCenter > y2:
            closeY = y2
        else:
            closeY = yCenter

        distanceX = xCenter - closeX
        distanceY = yCenter - closeY

        totalDistance = (distanceX * distanceX) + (distanceY * distanceY)
        squaredRadius = radius * radius

        return True if totalDistance <= squaredRadius else False