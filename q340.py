from collections import defaultdict


class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # edge case
        if len(s) == 0:
            return 0

        leftIndex = 0
        maxLen = 0
        letterCounts = defaultdict(lambda: 0)
        seenLetters = set()

        for rightIndex in range(len(s)):
            w = s[rightIndex]
            letterCounts[w] += 1
            if w not in seenLetters:
                seenLetters.add(w)

            while len(seenLetters) > k and leftIndex <= rightIndex:
                w = s[leftIndex]
                if w in seenLetters:
                    letterCounts[w] -= 1
                    if letterCounts[w] == 0:
                        seenLetters.remove(w)
                else:
                    assert False
                leftIndex += 1

            maxLen = max(maxLen, rightIndex - leftIndex + 1)

        return maxLen


if __name__ == "__main__":

    s = 'aba'
    k = 1
    print Solution().lengthOfLongestSubstringKDistinct(s, k)
