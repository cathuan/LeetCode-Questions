# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def construct_list(l):

    if len(l) == 0:
        return None

    head = ListNode(l[0])
    current_node = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        current_node.next = node
        current_node = node
    return head

def print_list(head):

    if head is None:
        return

    current_node = head
    while current_node is not None:
        print current_node.val,
        current_node = current_node.next
    print


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        current_head = head
        head_node, tail_node = self.reverseSubArray(current_head, k)
        new_head = head_node

        while head_node != current_head:
            current_head = tail_node.next
            prev_tail_node = tail_node
            head_node, tail_node = self.reverseSubArray(current_head, k)
            prev_tail_node.next = head_node

        return new_head

    def reverseSubArray(self, node, k):

        # check whether the rest of the list contains at least k nodes
        current_node = node
        valid_node_count = 0
        while current_node is not None:
            valid_node_count += 1
            current_node = current_node.next
            if valid_node_count == k:
                break

        if valid_node_count < k:
            return node, None
        node_after_tail = current_node

        count = 1

        previous_swap_node = node
        current_swap_node = node.next

        while count < k:
            buffer_node = current_swap_node.next
            current_swap_node.next = previous_swap_node
            previous_swap_node = current_swap_node
            current_swap_node = buffer_node
            count += 1

        node.next = current_swap_node
        return previous_swap_node, node


if __name__ == "__main__":

    head = construct_list([1,2,3,4,5,6,7,8,9])
    solution = Solution()
    new_head = solution.reverseKGroup(head, 4)
    print_list(new_head)
