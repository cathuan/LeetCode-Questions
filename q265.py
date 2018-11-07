class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        # min1 is used to store minimal cost up to house i-1.
        # min2 is used to store second minimal cost up to house i-1 given the house
        # i-1 is not painted with the same color as the minimal cost plan.
        # minIndex is used to store the color used to painted house i-1 for the
        # minimal cost plan.
        min1 = 0
        min2 = 0
        minIndex = -1

        for curCosts in costs:
            curMin1 = float("inf")
            curMin2 = float("inf")
            curMinIndex = -1

            # if we want to paint house i with color j, the minimal cost is
            #   - if j == minIndex, the minimal cost plan for the previus i-1 houses
            #     is use plan 2 (min2)
            #   - otherwise, other houses are paint with plan 1 (min1)
            # then calculate the minimal and second minimal plan for house i, and store
            # them for use in the next round.
            for j, cost in enumerate(curCosts):
                if j == minIndex:
                    curCost = cost + min2
                else:
                    curCost = cost + min1

                if curCost <= curMin1:  # curCost <= curMin1 < curMin2
                    curMin2 = curMin1
                    curMin1 = curCost
                    curMinIndex = j
                elif curCost <= curMin2:  # curMin1 < curCost <= curMin2
                    curMin2 = curCost
                else:  # curMin1 < curMin2 < curCost
                    pass

            # update min1, min2 and minIndex to use for the next round.
            min1 = curMin1
            min2 = curMin2
            minIndex = curMinIndex

        return min1
