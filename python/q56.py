# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals = sorted(intervals, key=lambda interval: interval.start)

        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
                continue

            prev = res[-1]
            assert prev.start <= interval.start
            if interval.start <= prev.end:
                if interval.end <= prev.end:
                    pass
                else:
                    prev.end = interval.end
            else:
                res.append(interval)

        return res