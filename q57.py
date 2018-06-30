class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

	def __repr__(self):
		return "[%s,%s]" % (self.start, self.end)


def getIntervals(intervals):

	ints = []
	for interval in intervals:
		int_ = Interval(interval[0], interval[1])
		ints.append(int_)
	return ints


class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""

		if len(intervals) == 0:
			return [newInterval]

		nums = [interval.start for interval in intervals]
		left_index = self.binarySearch(newInterval.start, nums)
		right_index = self.binarySearch(newInterval.end, nums)

		if left_index == -1:
			left_intervals = []
			left_interval_index = 0
			s = newInterval.start
		else:
			interval = intervals[left_index]
			if interval.end >= newInterval.start:
				if left_index == 0:
					left_intervals = []
					left_interval_index = 0
				else:
					left_intervals = intervals[:left_index]
					left_interval_index = left_index
				s = interval.start
			else:
				left_intervals = intervals[:left_index+1]
				s = newInterval.start

		if right_index == len(intervals)-1:
			right_intervals = []
		else:
			right_intervals = intervals[right_index+1:]
		right_interval_index = right_index

		if right_index == -1:
			e = newInterval.end
		else:
			e = max(intervals[right_index].end, newInterval.end)
		return left_intervals + [Interval(s,e)] + right_intervals

	def binarySearch(self, value, nums):

		if value < nums[0]:
			return -1
		if value >= nums[-1]:
			return len(nums)-1

		s = 0
		e = len(nums)-1
		mid = (s+e)/2
		while e - s > 1:
			if value >= nums[mid]:
				s = mid
			else:
				e = mid
			mid = (s+e)/2
		return s


if __name__ == '__main__':

	intervals = getIntervals([[1,2],[3,5],[6,7],[8,10],[12,16]])
	newInterval = Interval(4,8)
	print Solution().insert(intervals, newInterval)
		
		