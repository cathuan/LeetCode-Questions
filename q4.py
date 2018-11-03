class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if not nums1:
            return self.get_median(nums2)

        if not nums2:
            return self.get_median(nums1)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        start, end = 0, n1
        nums1 = [-float('inf')] + nums1 + [float('inf')]
        nums2 = [-float('inf')] + nums2 + [float('inf')]

        while True:
            eva_start, output_start = self.evaluate(start, nums1, nums2, n)
            if eva_start:
                return output_start

            eva_end, output_end = self.evaluate(end, nums1, nums2, n)
            if eva_end:
                return output_end

            mid = (start + end)/2
            eva_mid, output_mid = self.evaluate(mid, nums1, nums2, n)
            if eva_mid:
                return output_mid

            if output_mid == 'l':
                start = mid
            else:
                end = mid

    def get_median(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (nums[n/2-1] + nums[n/2])*1.0/2
        else:
            return nums[n/2]

    def evaluate(self, i1, nums1, nums2, n):

        i2 = n/2 - i1
        x1 = nums1[i1]
        y1 = nums1[i1+1]
        x2 = nums2[i2]
        y2 = nums2[i2+1]

        x, y = max(x1, x2), min(y1, y2)
        if x <= y:
            if n % 2 == 0:
                return True, (x+y)*1.0/2
            else:
                return True, float(y)
        else:
            if x1 > y2:
                return False, "r"
            elif x2 > y1:
                return False, 'l'
            else:
                assert False, "%s %s %s %s" % (x1, x2, y1, y2)


if __name__ == "__main__":
    nums1 = sorted([-0.727608348816,0.489120125846])
    nums2 = sorted([2.10799257546,0.0851689783126,3])
    print Solution().findMedianSortedArrays(nums1, nums2)