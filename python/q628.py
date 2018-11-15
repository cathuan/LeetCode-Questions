class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) >= 6:
            t1, t2, t3 = self.find_top_three(nums)
            b1, b2, b3 = self.find_bottom_three(nums)

            p1 = t1 * t2 * t3
            p2 = b1 * b2 * t1
            print t1, t2, t3, b1, b2, b3, p1, p2
        else:
            nums = sorted(nums)
            p1 = nums[-1] * nums[-2] * nums[-3]
            p2 = nums[0] * nums[1] * nums[-1]
        return max(p1, p2)

    def find_top_three(self, nums):

        n1, n2, n3 = None, None, None

        for num in nums:
            if n1 is None:
                n1 = num
            elif n2 is None:
                if num > n1:
                    n1, n2 = num, n1
                else:
                    n2 = num
            elif n3 is None:
                if num > n1:
                    n1, n2, n3 = num, n1, n2
                elif num > n2:
                    n1, n2, n3 = n1, num, n2
                else:
                    n3 = num
            else:
                if num > n1:
                    n1, n2, n3 = num, n1, n2
                elif num > n2:
                    n1, n2, n3 = n1, num, n2
                elif num > n3:
                    n1, n2, n3 = n1, n2, num

            print "max", n1, n2, n3, num

        return n1, n2, n3

    def find_bottom_three(self, nums):
        n1, n2, n3 = None, None, None

        for num in nums:
            if n1 is None:
                n1 = num
            elif n2 is None:
                if num < n1:
                    n1, n2 = num, n1
                else:
                    n2 = num
            elif n3 is None:
                if num < n1:
                    n1, n2, n3 = num, n1, n2
                elif num < n2:
                    n1, n2, n3 = n1, num, n2
                else:
                    n3 = num
            else:
                if num < n1:
                    n1, n2, n3 = num, n1, n2
                elif num < n2:
                    n1, n2, n3 = n1, num, n2
                elif num < n3:
                    n1, n2, n3 = n1, n2, num

        return n1, n2, n3


if __name__ == "__main__":

    nums = [7,3,1,0,0,6]
    solution = Solution()
    print solution.maximumProduct(nums)
