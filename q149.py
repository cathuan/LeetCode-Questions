# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict


class Solution(object):

    # going through all points p1 and p2 combinations.
    # one edge case is that p1 == p2, and this should be count to all the slopes.
    # remember we need to use gcd and (a,b) to record slope instead of float.
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        if len(points) <= 2:
            return len(points)

        ret = 0
        for i in range(len(points)):
            p1 = points[i]
            lines = defaultdict(int)
            localMax = 0
            overlapPoints = 0
            for j in range(i+1, len(points)):
                p2 = points[j]
                slope = self.getSlope(p1, p2)
                if slope != (0, 0):
                    lines[slope] += 1
                    localMax = max(localMax, lines[slope])
                else:
                    overlapPoints += 1
            ret = max(ret, overlapPoints + localMax + 1)
        return ret

    def getSlope(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        if dx != 0 and dy != 0:
            gcd = self.gcd(dx, dy)
            return (dx/gcd, dy/gcd)
        elif dx == 0 and dy == 0:
            return (0, 0)
        elif dx == 0 and dy != 0:
            return (0, 1)
        else:
            return (1, 0)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
