import bisect


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(%s, %s)" % (self.start, self.end)


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if len(self.intervals) == 0:
            self.intervals.append(Interval(val, val))
            return

        rightNodes = [interval.end for interval in self.intervals]
        # x_{i-1} < val <= x_i
        index = bisect.bisect_left(rightNodes, val)
        if index == 0:
            interval = self.intervals[0]
            if val < interval.start - 1:
                self.intervals = [Interval(val, val)] + self.intervals
            elif val == interval.start - 1:
                interval.start = val
            else:
                pass
        elif index == len(self.intervals):
            prevInterval = self.intervals[-1]
            if val > prevInterval.end + 1:
                self.intervals.append(Interval(val, val))
            elif val == prevInterval.end + 1:
                prevInterval.end = val
            else:
                pass
        else:
            interval = self.intervals[index]
            prevInterval = self.intervals[index - 1]
            if val >= interval.start:
                pass
            elif val == interval.start - 1:
                if val == prevInterval.end + 1:
                    self.intervals[index - 1:index + 1] = [Interval(prevInterval.start, interval.end)]
                else:
                    interval.start = val
            else:
                if val == prevInterval.end + 1:
                    prevInterval.end = val
                else:
                    self.intervals[index - 1:index + 1] = [prevInterval, Interval(val, val), interval]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


if __name__ == "__main__":

    obj = SummaryRanges()
    obj.addNum(6)
    print obj.getIntervals()
    obj.addNum(6)
    print obj.getIntervals()
    obj.addNum(0)
    print obj.getIntervals()
    obj.addNum(4)
    print obj.getIntervals()
    obj.addNum(8)
    print obj.getIntervals()
    obj.addNum(7)
    print obj.getIntervals()
    obj.addNum(6)
    print obj.getIntervals()
    obj.addNum(4)
    print obj.getIntervals()
    obj.addNum(7)
    print obj.getIntervals()
    obj.addNum(5)
    print obj.getIntervals()

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()