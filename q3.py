from collections import deque

class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_length = 0

        substring = deque()
        
        for i in range(len(s)):
            
            c = s[i]
            if c not in substring:
                substring.append(c)
                continue
            max_length = max(max_length, len(substring))

            if i < len(s) - 1:
                while c != substring.popleft():
                    pass
                substring.append(c)
        
        max_length = max(max_length, len(substring))
        return max_length


if __name__ == "__main__":

    solution = Solution()

    s = solution.lengthOfLongestSubstring("abcdefghijklmnacgfdsahyioewhfiughbdfnakohaifryuwemoifhifjdgisjadfoihdfgdsjfh"*5000)
    print s
    
