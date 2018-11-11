class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """

        lengthCount = len(R)/4+1
        L, R = int(L), int(R)
        count = 0
        for num in range(1, 10**lengthCount):
            num = str(num)
            if self.isSquareSuperPalindrome(int(num+num[::-1]), L, R):
                count += 1
            if self.isSquareSuperPalindrome(int(num[:-1]+num[::-1]), L, R):
                count += 1
        return count

    def isSquareSuperPalindrome(self, num, L, R):
        if num**2 < L or num**2 > R:
            return False
        if not self.isPalindrome(num**2):
            return False
        return True

    def isPalindrome(self, num):
        s = str(num)
        return s == s[::-1]


if __name__ == "__main__":

    L = "1"
    R = "999999999999999999"
    print Solution().superpalindromesInRange(L,R)