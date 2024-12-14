from typing import List


class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        # Map to maintain sorted frequency map of current window.
        # freq is a dictionary with freq[num] = number of element exists in current sliding window
        # will delete an element if the freq is 0
        freq = {}
        left = right = 0
        count = 0  # Total count of valid subarrays

        # In this while loop, essentially we increase the index of right end of sliding window by 1 each iteration
        # and make sure the sliding window is the longest continuous sub array with right end at the index
        while right < len(nums):
            # Add current element to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1
            right += 1

        return count

