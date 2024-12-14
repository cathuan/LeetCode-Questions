from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = []

        if len(s) < 10:
            return ans

        for i in range(len(s)-9):
            sequence = s[i:i+10]
            if sequence in seen:
                if sequence not in ans:
                    ans.append(sequence)
            else:
                seen.add(sequence)
            print(i, sequence, seen, ans)
        return ans