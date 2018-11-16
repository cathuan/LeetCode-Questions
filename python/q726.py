class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        tokens = self.tokenize(formula)
        stack = self.parse(tokens)
        return self.count(stack)

    def count(self, stack):
        atoms = {}
        for atom, count in stack:
            if atom not in atoms:
                atoms[atom] = 0
            atoms[atom] += count
        ret = ""
        for key, value in sorted(atoms.items()):
            if value > 1:
                ret += key + str(value)
            else:
                ret += key
        return ret

    def parse(self, tokens):
        stack = []
        for token in tokens:
            if token.isdigit():
                repeat = int(token)
                atom, count = stack.pop()
                assert count == 1
                if atom != ")":
                    stack.append((atom, repeat))
                else:
                    tmp = []
                    atom, count = stack.pop()
                    while atom != "(":
                        tmp.append((atom, count*repeat))
                        atom, count = stack.pop()
                    for elem in tmp:
                        stack.append(elem)
            else:
                stack.append((token, 1))
        return stack

    def tokenize(self, formula):
        tokens = []
        curElem = ""
        for w in formula:
            if w.isdigit():
                if curElem.isdigit():
                    curElem += w
                elif curElem:
                    tokens.append(curElem)
                    curElem = w
                else:
                    curElem = w
            elif w == "(" or w == ")":
                if curElem:
                    tokens.append(curElem)
                    curElem = ""
                tokens.append(w)
            elif w.isupper():
                if curElem.isdigit():
                    tokens.append(curElem)
                    curElem = w
                elif curElem:
                    tokens.append(curElem)
                    curElem = w
                else:
                    curElem = w
            else:
                curElem += w

        if curElem:
            tokens.append(curElem)

        return tokens


if __name__ == "__main__":

    formula = "Be32(Hoo2N3)11"
    print Solution().countOfAtoms(formula)
