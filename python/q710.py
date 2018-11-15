import random


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = sorted(blacklist)
        self.randomN = N - len(blacklist)

    def pick(self):
        """
        :rtype: int
        """
        randomNumber = random.randint(0, self.randomN-1)
        return self.getValue(randomNumber)

    def getValue(self, randomNumber):
        if len(self.blacklist) == 0:
            return randomNumber

        if len(self.blacklist) == 1:
            if randomNumber < self.blacklist[0]:
                return randomNumber
            else:
                return randomNumber + 1

        lo, hi = 0, len(self.blacklist)-1
        if randomNumber < self.blacklist[lo]:
            return randomNumber
        if hi + randomNumber >= self.blacklist[hi]:
            return hi + randomNumber + 1

        mid = (lo + hi)/2
        while hi - lo > 1:
            if randomNumber + mid < self.blacklist[mid]:
                hi = mid
            else:
                lo = mid
            mid = (lo + hi) / 2
        return hi + randomNumber


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()