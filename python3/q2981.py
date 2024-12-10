# Runtime: 7ms 90.54%
# Memory: 17.27MB 13.91%
class Solution:

    def maximumLength(self, s: str) -> int:
        # Go through the string and find the number of concatenation of each character.
        # counts: char -> [num1, num2, num3] where num1 >= num2 >= num3
        counts = {}

        current_count = 1
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                current_count += 1
            else:
                char = s[idx]
                if char not in counts:
                    counts[char] = [0, 0, 0]
                current_counts = counts[char]
                current_counts.append(current_count)
                current_counts.sort(reverse=True)
                counts[char] = current_counts[:3]
                current_count = 1

        char = s[idx+1]
        if char not in counts:
            counts[char] = [0, 0, 0]
        current_counts = counts[char]
        current_counts.append(current_count)
        current_counts.sort(reverse=True)
        counts[char] = current_counts[:3]
        current_count = 1

        ans = -1
        for char, (num1, num2, num3) in counts.items():
            if num1 == 1 and num2 == num3 == 0:
                ans = max(ans, -1)
            elif num1 == 2 and num2 == num3 == 0:
                ans = max(ans, -1)
            elif num1 == num2 == 1 and num3 == 0:
                ans = max(ans, -1)
            elif num1 == num2 and num1 == num3:
                ans = max(ans, num1)
            elif num1 == num2 and num1 > num3:
                ans = max(ans, num1 - 1)
            elif num1 == num2 + 1:
                ans = max(ans, num1 - 1)
            elif num1 > num2 + 1:
                ans = max(ans, num1 - 2)
        return ans


if __name__ == "__main__":
    s = "aca"
    print(Solution().maximumLength(s))