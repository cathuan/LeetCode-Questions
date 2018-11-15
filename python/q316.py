# -*- coding: utf-8 -*

import sys


class Solution(object):
    
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 找到所有字母最后出现时的index
        lastIndex = {}
        for i in range(len(s)):
            c = s[i]
            lastIndex[c] = i
        
        stack = []  # store index of character in s
        seen = set()
        for i in range(len(s)):
            c = s[i]

            # 当出现新字母的时候，如果stack之前的那个字母：1. 不是最后一次出现，2. 字母表顺序大于当前字母。
            # 那么，我们就可以把上一个字母pop出来。
            # 这个过程是持续的，一直到无法pop为止，比如在bcabc中，a需要pop掉它之前的b和c。
            while len(stack) > 0 and s[stack[-1]] >= c:
                # 如果是重复的，那么用最新的替代
                if s[stack[-1]] == c:
                    seen.remove(s[stack[-1]])
                    stack.pop()
                    break
                # 如果在i后面还有新的s[stack[-1]]，那么我们可以pop它。否则是不可以的。
                elif lastIndex[s[stack[-1]]] > i:
                    # 不重复push一样的char
                    if c not in seen:
                        seen.remove(s[stack[-1]])
                        stack.pop()
                    else:
                        break
                else:
                    break

            if c not in seen:
                stack.append(i)
                seen.add(c)

        result = ""
        for i in stack:
            result += s[i]
        return result


if __name__ == '__main__':
    print Solution().removeDuplicateLetters(sys.argv[1])