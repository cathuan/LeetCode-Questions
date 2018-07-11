class Solution(object):

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        
        sameCharLength = [1]
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            sameCharLength.append(count)

        dp = [1]
        chars = [[s[0]]]

        for i in range(1, len(s)):
            if len(chars[-1]) == 1:
                dp.append(dp[-1] + 1)
                newChar = list(set([chars[-1][0], s[i]]))
                chars.append(newChar)
            else:
                if s[i] in chars[-1]:
                    dp.append(dp[-1]+1)
                    newChar = chars[-1]
                    chars.append(newChar)
                else:
                    dp.append(sameCharLength[i-1]+1)
                    chars.append([s[i], s[i-1]])
        return max(dp)


if __name__ == "__main__":

    import sys
    print Solution().lengthOfLongestSubstringTwoDistinct(sys.argv[1])
