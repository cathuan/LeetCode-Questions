from collections import deque


class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        queue = deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B:
                return seen[S]
            for T in self.neighbors(S, B):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

    # use generator to save memory
    def neighbors(self, S, B):
        # find the first unmatching char
        for i, c in enumerate(S):
            if c != B[i]:
                break

        # for simplity modify S, need to convert it into list
        T = list(S)
        for j in range(i+1, len(S)):
            if S[j] == B[i]:
                T[i], T[j] = T[j], T[i]
                yield "".join(T)
                T[j], T[i] = T[i], T[j]
