class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        digit = ""
        for w in s:
            if w.isdigit():
                digit += w
            else:
                if digit:
                    stack.append(digit)
                    digit = ""
                stack.append(w)
                if w == "]":
                    stack = self.expand(stack)
        
        return "".join(stack)

    def expand(self, stack):

        assert stack.pop() == "]"
        content = stack.pop()
        contents = []
        while content != "[":
            contents.append(content)
            content = stack.pop()
        contents.reverse()
        content = "".join(contents)

        repeat = int(stack.pop())
        fmt = "".join([content for _ in range(repeat)])

        stack.append(fmt)
        return stack

        
if __name__ == "__main__":

    s = "3[a2[c]]"
    print Solution().decodeString(s)