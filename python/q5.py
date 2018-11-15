from collections import deque

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        even = self.get_even_strings(s)
        odd = self.get_odd_strings(s)

        return even if len(even) > len(odd) else odd

    def get_even_strings(self, s):

        buffered = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                buffered.append((i,i+1, deque([s[i], s[i+1]])))

        result = ""
        while len(buffered) > 0:
            result = "".join(buffered[0][2])
            buffered = self.extend_buffer(buffered, s)

        return result

    def get_odd_strings(self, s):

        buffered = []
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                buffered.append((i,i+2, deque([s[i], s[i+1], s[i+2]])))

        result = s[0]
        while len(buffered) > 0:
            result = "".join(buffered[0][2])
            buffered = self.extend_buffer(buffered, s)

        return result

    def extend_buffer(self, buffered, s):
        new_buffer = []

        for i, j, substring in buffered:
            if i > 0 and j < len(s) - 1 and s[i-1] == s[j+1]:
                substring.appendleft(s[i-1])
                substring.append(s[j+1])
                new_buffer.append((i-1, j+1, substring))

        return new_buffer


if __name__ == "__main__":

    solution = Solution()

    s = solution.longestPalindrome("a")
    print s
    
