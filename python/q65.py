import sys

class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()
        if s == "":
            return False

        first_char = s[0]

        # remove the sign at front
        if first_char == "+" or first_char == "-":
            s = s[1:]

        # handle .
        if "." in s and "e" not in s:
            return self.is_float_without_sign(s)
        elif "e" in s:
            segs = s.split("e")
            assert len(segs) > 1
            if len(segs) > 2:
                return False

            left_part, right_part = segs
            if left_part == "":
                return False

            if right_part == "":
                return False

            if "." in left_part:
                return self.is_float_without_sign(left_part) and self.is_integer(right_part)
            else:
                return self.is_integer_without_sign(left_part) and self.is_integer(right_part)
        else:
            return self.is_integer_without_sign(s)


    def is_float_without_sign(self, s):
        segs = s.split(".")
        assert len(segs) > 1
        if len(segs) > 2:
            return False

        left_part, right_part = segs
        if left_part == "":
            return self.is_integer_without_sign(right_part)
        else:
            return self.is_integer_without_sign(left_part) and (self.is_integer_without_sign(right_part) or right_part == "")

    def is_integer_without_sign(self, s):

        if len(s) == 0:
            return False
        for char in s:
            if not char.isdigit():
                return False
        return True

    def is_integer(self, s):

        if len(s) == 0:
            return False
        first_char = s[0]
        # remove the sign at front
        if first_char == "+" or first_char == "-":
            s = s[1:]

        return self.is_integer_without_sign(s)


if __name__ == "__main__":

    s = sys.argv[1]
    solution = Solution()
    print solution.isNumber(s)
