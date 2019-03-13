class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        ret = []
        nums = [lower] + nums + [upper]
        for i in range(len(nums)-1):
            v1, v2 = nums[i], nums[i+1]
            if i == 0:
                v1 = v1 - 1
            if i == len(nums)-2:
                v2 = v2 + 1

            diff = self.getDiff(v1, v2)
            if diff is not None:
                ret.append(diff)
        return ret

    def getDiff(self, v1, v2):

        assert v1 <= v2
        if v1 == v2:
            return None
        elif v1 == v2 - 1:
            return None
        elif v1 == v2 - 2:
            return str(v1+1)
        else:
            return "%s->%s" % (v1+1,v2-1)


if __name__ == "__main__":

    print Solution().findMissingRanges([0,1,3,50,75], 0, 99)
    print Solution().findMissingRanges([0], 0, 0)
    print Solution().findMissingRanges([0], 0, 1)
    print Solution().findMissingRanges([], 0, 1)
    print Solution().findMissingRanges([], 0, 0)
    print Solution().findMissingRanges([], 0, 2)