import bisect


class RangeModule(object):
    def __init__(self):
        self.ranges = []

    # find i such that y_{i-1} < left <= y_i
    # find j such that x_j <= right < x_{j+1}
    # Therefore, self.ranges[i:j+1] intersect with [left, right)
    def _getBounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in [100, 10, 1]:
            while i + d - 1 < len(
                    self.ranges) and self.ranges[i + d - 1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j - d + 1][0] > right:
                j -= d
        return i, j

    # replace (x_i, y_i), ..., (x_j, y_j) with union of them and (left, right)
    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i, j = self._getBounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j + 1] = [(left, right)]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        if not self.ranges:
            return False

        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        i = i - 1 if i > 0 else i
        return self.ranges[i][0] <= left and right <= self.ranges[i][1]

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i, j = self._getBounds(left, right)
        merge = []
        for k in range(i, j + 1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j + 1] = merge


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)