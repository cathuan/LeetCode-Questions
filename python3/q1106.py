from typing import List


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # There are three operators, !, &, and |. All come with op(exp, exp).
        # So we use stack to store everything, and whenever we see a ")", we find the previous "(" and evaluate.
        stack = []

        for char in expression:
            if char == ")":
                exps = []
                while stack[-1] != "(":
                    new_char = stack.pop()
                    if new_char == ",":
                        continue
                    exps.append(new_char)
                stack.pop()  # remove "("
                operator = stack.pop()  # get !, &, or |
                new_exp = self.derive(operator, exps)
                stack.append(new_exp)
            else:
                stack.append(char)
        
        return stack.pop() == 't'

    def derive(self, operator: str, exps: List[str]) -> str:
        if operator == "!":
            return 'f' if exps[0] == 't' else 't'

        # AND, 't' if all are 't' else 'f'
        if operator == '&':
            for exp in exps:
                if exp == 'f':
                    return 'f'
            return 't'

        # OR, 't' if any is 't' else 'f'
        if operator == '|':
            for exp in exps:
                if exp == 't':
                    return 't'
            return 'f'

