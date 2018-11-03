from __future__ import print_function


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        segs = input.split("\n")
        stack = []
        current_path = ""
        max_abs_path = 0

        for seg in segs:
            level, name = self.get_level(seg)
            while level < len(stack):
                stack.pop()

            stack.append(name)
            current_path = "/".join(stack)

            if "." in name:
                max_abs_path = max(max_abs_path, len(current_path))

        return max_abs_path

    def get_level(self, seg):
        level = 0
        i = 0
        while seg[i] == "\t":
            level += 1
            i += 1
        return level, seg[i:]


if __name__ == "__main__":

    s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution().lengthLongestPath(s))
