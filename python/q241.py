import re
import operator


class BracketTemplate(object):

    @staticmethod
    def construct_templates(operands):
        """
        :type input: List[str]
        :rtype: List[str]
        """

        raw_templates = BracketTemplate.construct_template_without_detailed_operands(len(operands))
        return [BracketTemplate.create_template(raw_template, operands) for raw_template in raw_templates]

    @staticmethod
    def create_template(raw_template, operands):
        return "%s".join(("%s".join(raw_template.split("O")) % tuple(operands)).split("D"))

    @staticmethod
    def construct_template_without_detailed_operands(n_operands):
        # D represents digits
        # O represents operands
        if n_operands == 0:
            return set(["(D)"])

        templates = BracketTemplate.construct_template_without_detailed_operands(n_operands-1)
        template_lists = [template.split("D") for template in templates]
        # there are n_operands D in last_template. The list has n_operands+1 elements.

        #raw_templates = ["D".join(template_list[:i] + [template_list[i]+"(DOD)"+template_list[i+1]] + template_list[i+2:])
        #      for template_list in template_lists for i in range(n_operands)]
        #raw_templates = set(raw_templates)
        raw_templates = set()
        for template_list in template_lists:
            for i in range(n_operands):
                new_template = "D".join(template_list[:i] + [template_list[i]+"(DOD)"+template_list[i+1]] + template_list[i+2:])
                raw_templates.add(new_template)

        return raw_templates


# TODO: slow, bad. It's only 13.14%...
# eval() is evil. Don't do that. Maybe use operator.add/mul or so instead? Write a AST and work with it.
class Solution2(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        operands = self.get_operands(input)
        numbers = self.get_numbers(input)
        templates = BracketTemplate.construct_templates(operands)
        exprs = [template % numbers for template in templates]
        solutions = [eval(expr) for expr in exprs]  # XXX: very dangerous!
        return sorted(solutions)

    def get_operands(self, input):
        operands = []
        unmatched_bracket_counts = 0
        for i in range(len(input)):
            char = input[i]
            if char == "(":
                unmatched_bracket_counts += 1
            elif char == ")":
                unmatched_bracket_counts -= 1
            elif char in ["+", "-", "*"] and unmatched_bracket_counts == 0:
                assert i != 0
                operands.append(char)
        return operands

    def get_numbers(self, input):

        input = "O".join(input.split("+"))
        input = "O".join(input.split("-"))
        input = "O".join(input.split("*"))
        return tuple(input.split("O"))


# Way faster.. Happier now. 39ms and 80.66%.
class Solution(object):

    def diffWaysToCompute(self, input):

        # very simple AST. Split operators and numbers.
        tokens = re.split('(\\D)', input)
        self.nums = map(int, tokens[::2])
        operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        self.operators = map(lambda s: operator_dict[s], tokens[1::2])

        return self.construct_results(0, len(self.nums) - 1)

    def construct_results(self, i, j):

        # base case
        if i == j:
            return [self.nums[i]]

        # determine the first bracket split place.
        # because any two valid items must be bracketed, there will not be duplicated result!
        return [self.operators[operator_index](left_result, right_result)
                for operator_index in xrange(i, j)
                for left_result in self.construct_results(i, operator_index)
                for right_result in self.construct_results(operator_index + 1, j)]


if __name__ == "__main__":

    input = "1-2+3*4-5*6-7+8*9"
    #input = "0"
    Solution().diffWaysToCompute(input)
    Solution2().diffWaysToCompute(input)

    #operands = ["+", "-", "+", "-", "+", "-", "+", "-"]
    #result = BracketTemplate().construct_templates(operands)
    #print result
