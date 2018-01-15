import sys
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_counts = Counter()
        for char in t:
            t_counts[char] += 1

        chars = t_counts.keys()




if __name__ == "__main__":

    s = sys.argv[1]
    t = sys.argv[2]

    print Solution().minWindow(s,t)
