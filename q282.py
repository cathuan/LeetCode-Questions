import sys


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        if len(num) == 1:
            if int(num) == target:
                return [num]
            return []

        nums = [int(i) for i in num]
        res = []
        
        def dfs(i, expr, prod, prevSum, curr):
            """
            previous result can be interpreted as: a product of a sequence of numbers + a prevous result
            :param i: position in num
            :param expr: current expression
            :param prod: current product, e.g. 2*1*3 for '2*4+0+2*1*3'
            :param prevSum: value of expression before product, e.g. 2*4+0=0 for '2*4+0+2*1*3'
            :param curr: most recent number, e.g. 21 in expression '20+21' 
            """
            if i == len(nums)-1:
                if prevSum + prod + nums[i] == target:
                    res.append(expr + '+' + str(nums[i]))
                if prevSum + prod - nums[i] == target:
                    res.append(expr + '-' + str(nums[i]))
                if prevSum + prod*nums[i] == target:
                    res.append(expr + '*' + str(nums[i]))
                # prod = prevProd*curr; 
                # new_prod = prevProd*(curr*10+nums[i]) = 10*prod + prod//curr*nums[i]
                if curr and 10*prod + prod//curr*nums[i] + prevSum == target:
                    res.append(expr+str(nums[i]))
            else:
                dfs(i+1, expr+'+'+str(nums[i]), nums[i], prod+prevSum, nums[i])
                dfs(i+1, expr+'-'+str(nums[i]), -nums[i], prod+prevSum, nums[i])
                dfs(i+1, expr+'*'+str(nums[i]), nums[i]*prod, prevSum, nums[i])
                if curr:
                    # append nums[i] directly to last number, impossible when last number is 0
                    dfs(i+1, expr+str(nums[i]), 10*prod + prod//curr*nums[i], prevSum, 10*curr+nums[i])
        
        dfs(1, str(nums[0]), nums[0], 0, nums[0])
        return res
        

if __name__ == '__main__':

    print Solution().addOperators(sys.argv[1], int(sys.argv[2]))




