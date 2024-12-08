# Runtime: 7ms beats 31.42%
# Memory: 17.26MB Beats 14.64%
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_node = None

        curr_node_1 = l1
        curr_node_2 = l2
        extra_to_next_digit = 0

        while (
            curr_node_1 is not None
            or curr_node_2 is not None
            or extra_to_next_digit != 0
        ):
            # Handle the special case when the running out of two lists but we still have 1 extra needs to add
            if curr_node_1 is None and curr_node_2 is None and extra_to_next_digit != 0:
                curr_result_node.next = ListNode(val=1)
                extra_to_next_digit = 0
                continue

            # connect node in the next node.
            # Need to do it at the beginning of the loop. Otherwise we may have an extra 0 on the top.
            if result_node is None:
                result_node = ListNode()
                curr_result_node = result_node
            else:
                curr_result_node.next = ListNode()
                curr_result_node = curr_result_node.next

            curr_value_1 = curr_node_1.val if curr_node_1 else 0
            curr_value_2 = curr_node_2.val if curr_node_2 else 0
            curr_sum = curr_value_1 + curr_value_2 + extra_to_next_digit
            if curr_sum < 10:
                curr_result_node.val = curr_sum
                extra_to_next_digit = 0
            else:
                curr_result_node.val = curr_sum - 10
                extra_to_next_digit = 1

            if curr_node_1 is not None:
                curr_node_1 = curr_node_1.next
            if curr_node_2 is not None:
                curr_node_2 = curr_node_2.next

        return result_node
