# Runtime: 7ms, 43.56%
# Memory: 17.27MB, 11.06%

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000,
        }

        ans = 0
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == 'I':
                if idx < len(s)-1 and s[idx+1] == "V":
                    ans += 4
                    idx += 2
                elif idx < len(s)-1 and s[idx+1] == "X":
                    ans += 9
                    idx += 2
                else:
                    ans += 1
                    idx += 1
            elif char == "X":
                if idx < len(s)-1 and s[idx+1] == "L":
                    ans += 40
                    idx += 2
                elif idx < len(s)-1 and s[idx+1] == "C":
                    ans += 90
                    idx += 2
                else:
                    ans += 10
                    idx += 1
            elif char == "C":
                if idx < len(s)-1 and s[idx+1] == "D":
                    ans += 400
                    idx += 2
                elif idx < len(s)-1 and s[idx+1] == "M":
                    ans += 900
                    idx += 2
                else:
                    ans += 100
                    idx += 1
            else:
                ans += values[char]
                idx += 1
        return ans