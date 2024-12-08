# Runtime: 264ms, Beats 36.41%
# Memory: 57.45MB, Beats 61.44%
import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # sort all events based on end time
        events.sort(key=lambda x: x[1])

        end_time_to_max_value = []
        curr_max_value = 0
        for start_time, end_time, event_value in events:
            curr_max_value = max(event_value, curr_max_value)
            end_time_to_max_value.append((end_time, curr_max_value))

        # Now for each event find the max value
        result = 0
        for start_time, end_time, event_value in events:
            result = max(result, event_value)

            # find the idx so that end_time_to_max_value[idx] is the first value such that
            # end_time_to_max_value[idx] >= (start_time, 0)
            idx = bisect.bisect_left(end_time_to_max_value, (start_time, 0)) - 1
            if idx >= 0:
                result = max(result, event_value + end_time_to_max_value[idx][1])

        return result