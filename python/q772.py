class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        op = "+"
        number = 0
        for w in s:
            if w.isdigit():
                number = number * 10 + int(w)
            elif w == "(":
                stack.append(op)
                op = "+"
            elif w == ")":
                self.helper(op, number, stack)
                val = 0
                while True:
                    curr = stack.pop()
                    if not isinstance(curr, int):
                        op = curr
                        break
                    val += curr
                number = val
            elif w != " ":
                self.helper(op, number, stack)
                number = 0
                op = w

        if number:
            self.helper(op, number, stack)
        return sum(stack)

    def helper(self, op, number, stack):
        if op == '+':
            stack.append(number)
        elif op == "-":
            stack.append(-number)
        elif op == "*":
            stack.append(stack.pop() * number)
        elif op == "/":
            stack.append(int(stack.pop() / number))


if __name__ == "__main__":

    s = "(2+6* 3+5- (3*14/7+2)*5)+3"
    print Solution().calculate(s)
