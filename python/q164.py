class Bucket(object):

    def __init__(self, num):
        self.min = num
        self.max = num

    def refresh(self, num):
        self.min = min(num, self.min)
        self.max = max(num, self.max)

    def __repr__(self):
        return "(%s,%s)" % (self.min, self.max)


class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        if len(nums) <= 1:
            return 0
        
        min_value = min(nums)
        max_value = max(nums)
        b = (max(nums) - min_value)/(len(nums)-1)

        if b == 0:
            return 0

        buckets = {}

        for num in nums:
            i = (num - min_value) / b + 1
            if i not in buckets:
                buckets[i] = Bucket(num)
            else:
                buckets[i].refresh(num)

        output = 0
        bs = [buckets[k] for k in sorted(buckets.keys())]
        for i in range(1, len(bs)):
            output = max(output, bs[i].min - bs[i-1].max)

        return output


if __name__ == "__main__":

    print Solution().maximumGap([1,1,1,1,1,5,5,5,5,5])