from fractions import Fraction


class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A) <= 1:
            return False

        totalSum = sum(A)
        average = Fraction(totalSum, len(A))
        A = [v - average for v in A]

        # we can always separate A as {0} and {A-0}
        if 0 in A:
            return True

        # assume no 0 in A
        A = [v for v in A if v != 0]
        n = len(A)/2

        frtHalf = A[:n]
        sndHalf = A[n:]

        left = set()
        for v in frtHalf:
            left = {value + v for value in left} | left | {v}
        if 0 in left:
            return True

        right = set()
        for v in sndHalf:
            right = {value + v for value in right} | right | {v}
        if 0 in right:
            return True

        frtSum = sum(frtHalf)
        for leftValue in left:
            if leftValue == frtSum:
                continue
            if -leftValue in right:
                return True
        return False
