from typing import List
from collections import deque
from heapq import heappush, heappop


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Initialize result to the maximum possible integer value
        shortest_subarray_length = float("inf")

        cumulative_sum = 0

        # Min-heap to store cumulative sum and its corresponding index
        prefix_sum_heap = []

        # Iterate through the array
        for i, num in enumerate(nums):
            # Update cumulative sum
            cumulative_sum += num

            # If cumulative sum is already >= k, update shortest length
            if cumulative_sum >= k:
                shortest_subarray_length = min(shortest_subarray_length, i + 1)

            # Remove subarrays from heap that can form a valid subarray
            # It's ok to remove it here since if we see another number later the subarray is always bigger.
            while (prefix_sum_heap and cumulative_sum - prefix_sum_heap[0][0] >= k):
                # Update shortest subarray length
                shortest_subarray_length = min(shortest_subarray_length, i - heappop(prefix_sum_heap)[1])

            # Add current cumulative sum and index to heap
            heappush(prefix_sum_heap, (cumulative_sum, i))

        # Return -1 if no valid subarray found
        if shortest_subarray_length == float("inf"):
            return -1
        else: 
            return shortest_subarray_length


class Solution2:

    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)

        # Size is n+1 to handle subarrays starting from index 0 (length 0 subarray)
        prefix_sums = [0] * (n + 1)

        # Calculate prefix sums
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()

        shortest_subarray_length = float("inf")

        for i in range(n + 1):
            # Remove candidates from front of deque where subarray sum meets target
            while (candidate_indices and prefix_sums[i] - prefix_sums[candidate_indices[0]] >= target_sum):
                # Update shortest subarray length
                shortest_subarray_length = min(shortest_subarray_length, i - candidate_indices.popleft())

            # Maintain monotonicity by removing indices with larger prefix sums
            while (candidate_indices and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]):
                candidate_indices.pop()

            # Add current index to candidates
            candidate_indices.append(i)

        # Return -1 if no valid subarray found
        if shortest_subarray_length == float('inf'):
            return -1
        else:
            return shortest_subarray_length