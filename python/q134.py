class SolutionSlow(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1

        total_gas, total_cost = 0, 0
        i = 0
        j = 0
        length = len(gas)
        while (i - 1) % length != j:
            #total_gas, total_cost = total_gas+gas[j], total_cost+cost[j]
            total_gas += gas[j]
            total_cost += cost[j]
            #print "+", i, j, total_gas, total_cost
            while total_gas < total_cost:
                #total_gas, total_cost = total_gas-gas[i], total_cost-cost[i]
                total_gas -= gas[i]
                total_cost -= cost[i]
                #print "-", i, j, total_gas, total_cost
                i = (i + 1) % length
            j = (j + 1) % length

        return i

import numpy as np


# Much faster
class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1

        gas = np.array(gas)
        cost = np.array(cost)

        diffs = gas.cumsum() - cost.cumsum()
        index = diffs.argmin()

        return (index+1) % len(gas)


if __name__ == "__main__":

    gas = [2]*100 + [4,5]
    cost = [1]*100 + [105,4]
    print Solution().canCompleteCircuit(gas, cost)
