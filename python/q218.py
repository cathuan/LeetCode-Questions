# here we use heapq to create a binary heap which has min value on the top.
# We need O(log(n)) to push and pop, and O(1) to achieve the minimum value.
# This is better than a plain sorted list.
from heapq import *


class Solution(object):
	
	def getSkyline(self, buildings):
		"""
		:type buildings: List[List[int]]
		:rtype: List[List[int]]
		"""

		positions = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
		currentBuildings = []
		result = []
		buildingIndex = 0
		prevHeight = 0

		for curPosition in positions:

			# remove passed buildings (only the top one)
			while len(currentBuildings) > 0 and curPosition >= currentBuildings[0][1]:
				heappop(currentBuildings)

			# record new appeared buildings. Since buildings are ordered, we can go through it only once.
			while buildingIndex < len(buildings) and buildings[buildingIndex][0] <= curPosition:
				heappush(currentBuildings, [-buildings[buildingIndex][2], buildings[buildingIndex][1]])
				buildingIndex += 1

			# use heap to find the highest building atm and refresh the height if necessary
			if len(currentBuildings) > 0:
				currentHeight = -currentBuildings[0][0]
				if currentHeight != prevHeight:
					result.append([curPosition, currentHeight])
					prevHeight = currentHeight
			else:
				result.append([curPosition, 0])

		return result


if __name__ == '__main__':

	print Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])



