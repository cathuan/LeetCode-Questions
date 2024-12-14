class Solution:
    def intToRoman(self, num: int) -> str:
        # I: 1
        # V: 5
        # X: 10
        # L: 50
        # C: 100
        # D: 500
        # M: 1000

        roman_digit = {
            0: {
                1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"
            },
            1: {
                1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC",
            },
            2: {
                1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM",
            },
            3: {
                1: "M", 2: "MM", 3: "MMM"
            }
        }

        curr_num = num
        level = 0
        ans = []
        while curr_num > 0:
            digit = curr_num % 10
            if digit > 0:
                ans.append(roman_digit[level][digit])
            curr_num = int((curr_num - digit) / 10)
            level += 1
        return "".join(ans[::-1])