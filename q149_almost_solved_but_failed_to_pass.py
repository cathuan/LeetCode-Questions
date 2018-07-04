# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)

class Line(object):

    def __init__(self, p1, p2, i1, i2):
        if p1.x == p2.x:
            if p1.y == p2.y:
                self.slope = float("inf")
                self.intercept = float("inf")
            else:
                self.slope = float("inf")
                self.intercept = p1.x
        else:
            self.slope = (p2.y-p1.y)*1.0/(p2.x-p1.x)
            self.intercept = p2.y - self.slope*p2.x
        self.containedPoints = set([i1,i2])

    def isOnLine(self, p, i):
        # if current points are all the same, any other point can form a new line with them
        if self.slope == float("inf") and self.intercept == float("inf"):
            self.containedPoints.add(i)
            return True
        # vertical line
        elif self.slope == float("inf") and self.intercept == p.x:
            self.containedPoints.add(i)
            return True
        # colinear and handle round error
        elif abs(self.slope * p.x + self.intercept - p.y) < 1e-6:
            self.containedPoints.add(i)
            return True
        else:
            return False

    def __repr__(self):
        return "Line: %s, %s, %s" % (self.slope, self.intercept, self.containedPoints)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1

        lines = []
        maxLine = None
        seenPoints = set()
        for i in range(len(points)):
            p = points[i]

            currentPoints = seenPoints
            if len(currentPoints) == 0:
                seenPoints.add(i)
                print "Start", p, seenPoints
                continue

            for line in lines:
                if line.isOnLine(p, i):
                    if maxLine is None or len(line.containedPoints) > len(maxLine.containedPoints):
                        maxLine = line
                    currentPoints = currentPoints - line.containedPoints
                if len(line.containedPoints) > 15:
                    print "Mod", i, p, line, len(line.containedPoints)


            for j in currentPoints:
                p_ = points[j]
                line = Line(p, p_, i, j)
                if maxLine is None:
                    maxLine = line
                print "New", p, line
                lines.append(line)

            seenPoints.add(i)

        return len(maxLine.containedPoints)


def listToPoint(l):
    points = []
    for x, y in l:
        points.append(Point(x,y))
    return points


if __name__ == "__main__":

    points = listToPoint([[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86]])
    print Solution().maxPoints(points)