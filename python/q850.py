from collections import defaultdict


class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        events = self.setEvents(rectangles)
        actives = []

        volume = 0
        eventYs = sorted(events.keys())
        for i in range(len(eventYs)-1):
            y1, y2 = eventYs[i], eventYs[i+1]
            for event, x1, x2 in events[y1]:
                if event == "add":
                    actives.append((x1, x2))
                else:
                    actives.remove((x1, x2))
            curLength = self.getLength(actives)
            volume += curLength * (y2-y1)
            #volume = volume % (1000*1000*1000)
        return volume % (10**9+7)

    def setEvents(self, rectangles):
        events = defaultdict(list)
        for x1, y1, x2, y2 in rectangles:
            events[y1].append(("add", x1, x2))
            events[y2].append(("remove", x1, x2))
        return events

    def getLength(self, actives):
        intervals = sorted(actives)
        curMaxX = -1
        curLength = 0
        for x1, x2 in intervals:
            curMaxX = max(x1, curMaxX)
            curLength += max(0, x2 - curMaxX)
            curMaxX = max(x2, curMaxX)
        return curLength