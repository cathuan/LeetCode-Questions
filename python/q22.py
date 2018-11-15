class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []

        left_parenthesis_count = n
        right_parenthesis_count = n
        result = []

        self.dfs(left_parenthesis_count, right_parenthesis_count, result, "")
        return result

    def dfs(self, left_parenthesis_count, right_parenthesis_count, result, cur_string):
        if left_parenthesis_count > right_parenthesis_count:
            return

        if left_parenthesis_count == 0 and right_parenthesis_count == 0:
            result.append(cur_string)
            return

        if left_parenthesis_count > 0:
            self.dfs(left_parenthesis_count-1, right_parenthesis_count, result, cur_string+"(")
        if right_parenthesis_count > 0:
            self.dfs(left_parenthesis_count, right_parenthesis_count-1, result, cur_string+")")


if __name__ == "__main__":

    n = 10
    Solution().generateParenthesis(n)
