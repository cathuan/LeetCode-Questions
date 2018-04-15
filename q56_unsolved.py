# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# TODO: merge findMaxTailLeftToInterval and findMinHeadRightToInterval.
# They are basically two binary search functions.

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

    def addNewInterval(self, intervals, new_interval):

        i = self.findMaxTailLeftToInterval(intervals, new_interval)
        j = self.findMinHeadRightToInterval(intervals, new_interval)

    # TODO: there are bugs here. Fix first. Need to organize the logic flow.
    def findMaxTailLeftToInterval(self, intervals, new_interval):
        if len(intervals) == 0:
            return -1

        i = 0
        j = len(intervals)-1

        if intervals[[j].end < new_interval.start:
            return j

        if intervals[i].end >= new_interval.start:
            return -1

        mid = (i + j)//2
        while j - i > 1:
            if intervals[mid].end == new_interval.start:
                return mid

            if intervals[mid].end < new_interval.start:
                i = mid
            elif intervals[mid].end > new_interval.start:
                j = mid

        return i

    def findMinHeadRightToInterval(self, intervals, new_interval):
        if len(intervals) == 0:
            return -1

        i = 0
        j = len(intervals)-1

        if intervals[[i].start >= new_interval.end:
            return i

        if intervals[j].start < new_interval.end:
            return len(intervals)

        mid = (i + j)//2
        while j - i > 1:
            if intervals[mid].start == new_interval.end:
                return mid

            if intervals[mid].start < new_interval.end:
                i = mid
            elif intervals[mid].start > new_interval.end:
                j = mid

        return j
