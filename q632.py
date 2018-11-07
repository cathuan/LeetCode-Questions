import heapq


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, v):
        heapq.heappush(self.heap, v)

    def pop(self):
        return heapq.heappop(self.heap)

    def getMin(self):
        if not self.heap:
            return None
        return self.heap[0]

    def getLength(self):
        return len(self.heap)


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        nArrays = len(nums)

        # pointers records the current chosen elements of each array.
        pointers = [0] * nArrays
        minHeap = MinHeap()

        # minValue, maxValue record current minimum and maximum value of chosen elements.
        # They automatically form the current range.
        maxValue = -float('inf')
        for i in range(nArrays):
            minHeap.push((nums[i][0], i))
            maxValue = max(maxValue, nums[i][0])
        minValue, _ = minHeap.getMin()

        # current minimal range
        minRange = maxValue - minValue
        curRange = [minValue, maxValue]

        # The maxValue is not modifiable. Decreasing max is equivalently repeating
        # previous steps. Hence we keep increasing minValue and update current
        # maxValue and minValue.

        # Keep tracking the current min/maxValues and record best range we have seen
        # so far.

        # Whenever a minValue is the highest value of its list, it means we are not
        # able to keep running the process again, and we exit.
        while True:
            _, arrayIndex = minHeap.pop()
            valueIndex = pointers[arrayIndex]
            if valueIndex == len(nums[arrayIndex]) - 1:
                break
            newValueIndex = valueIndex + 1
            pointers[arrayIndex] += 1
            newNum = nums[arrayIndex][newValueIndex]
            minHeap.push((newNum, arrayIndex))
            maxValue = max(maxValue, newNum)
            minValue, _ = minHeap.getMin()
            if maxValue - minValue < minRange:
                minRange = maxValue - minValue
                curRange = [minValue, maxValue]

        return curRange