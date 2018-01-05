import sys

MAX_INT = 2147483647
MIN_INT = -2147483648


# 68% quantile
class Solution(object):

    def divide_by_part(self, dividend, divisor):

        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        remainder = "" if dividend == 0 else str(dividend)
        return str(result), remainder

    def divide_two_positives(self, dividend, divisor):

        dividend_str = str(dividend)
        divisor_str = str(divisor)
        length = len(divisor_str)

        results = []
        remainder = dividend_str[:length-1]
        for i in range(length-1, len(dividend_str)):
            dividend_part = int(remainder + dividend_str[i])
            result, remainder = self.divide_by_part(dividend_part, divisor)
            results.append(result)
        solution = "".join(results)
        solution = solution if solution != "" else "0"
        return solution

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        dividend_sign = -1 if dividend < 0 else 1
        divisor_sign = -1 if divisor < 0 else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 0:
            result = sys.maxint
        elif divisor == 1:
            result = dividend
        else:
            result = int(self.divide_two_positives(dividend, divisor))

        if dividend_sign == divisor_sign:
            result = result
        else:
            result = -result

        result = result if result < MAX_INT else MAX_INT
        result = result if result > MIN_INT else MIN_INT

        return result


if __name__ == "__main__":

    dividend = int(sys.argv[1])
    divisor = int(sys.argv[2])

    solution = Solution()
    print solution.divide(dividend, divisor)
