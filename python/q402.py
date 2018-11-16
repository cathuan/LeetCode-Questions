class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if len(num) == 0:
            return "0"

        stack = []
        for w in num:
            n = int(w)
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        stack.reverse()
        while stack and stack[-1] == 0:
            stack.pop()
        stack.reverse()

        if not stack:
            return "0"

        return "".join(str(v) for v in stack)


if __name__ == "__main__":

    num = "1432219"
    k = 3
    print Solution().removeKdigits(num, k)
