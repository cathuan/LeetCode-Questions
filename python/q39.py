# FIXME: Unfinished at all.


class Solution:

    def __init__(self):
        self.stack = []
        self.results = {}

    def combinationSum(self, candidates, target: int):
        self.stack.append(target)
        candidates = sorted(candidates)
        while len(self.stack) > 0:
            self.expand(candidates)

        return self.results[target]

    def expand(self, candidates):
        v = self.stack[-1]
        if v not in self.results:
            self.results[v] = []
        for candidate in candidates:
            if candidate > v:
                continue
            pass


if __name__ == "__main__":

    candidates = {2,3,6,7}
    target = 7
    print(Solution().combinationSum(candidates, target))