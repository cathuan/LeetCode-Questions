from collections import deque
import copy


class Solution(object):

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        variables = {}
        return self.processExpr(expression, variables)

    def processExpr(self, expression, variables):
        stack = deque(self.parse(expression))
        op = stack.popleft()
        if op == "add":
            var1 = stack.popleft()
            var2 = stack.popleft()

            var1 = self.processToken(var1, variables)
            var2 = self.processToken(var2, variables)
            output = var1 + var2
        elif op == "mult":
            var1 = stack.popleft()
            var2 = stack.popleft()

            var1 = self.processToken(var1, variables)
            var2 = self.processToken(var2, variables)
            output = var1 * var2
        elif op == "let":
            while stack:
                if len(stack) == 1:
                    expr = stack.popleft()
                    output = self.processToken(expr, variables)
                else:
                    var = stack.popleft()
                    val = stack.popleft()
                    val = self.processToken(val, variables)
                    variables[var] = val
        return output

    def parse(self, expression):
        stack = []
        assert expression[0] == "("
        assert expression[-1] == ")"
        bracketCount = 0
        token = ''
        for index in range(1, len(expression)-1):
            if expression[index] == '(':
                bracketCount += 1
                token += '('
            elif expression[index] == ')':
                bracketCount -= 1
                token += ')'
                if bracketCount == 0:
                    stack.append(token)
                    token = ''
            else:
                if expression[index].isspace():
                    if bracketCount > 0:
                        token += expression[index]
                    else:
                        if token:
                            stack.append(token)
                            token = ''
                else:
                    token += expression[index]

        if token:
            stack.append(token)
            token = ''
        return stack

    def isExpr(self, token):
        return token[0] == '(' and token[-1] == ')'

    def isDigit(self, token):
        if token[0] == '-':
            return token[1:].isdigit()
        return token.isdigit()

    def processToken(self, token, variables):
        if self.isExpr(token):
            return self.processExpr(token, copy.copy(variables))
        elif self.isDigit(token):
            return int(token)
        else:
            return variables[token]


if __name__ == "__main__":

    print Solution().processExpr("(let x 7 -12)", {})
