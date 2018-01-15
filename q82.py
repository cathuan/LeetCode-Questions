# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import LinkedList as L

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if it is an empty list
        if head is None:
            return head

        prev_node = None
        current_node = head
        new_head = head

        while current_node is not None:

            if self.peek(current_node):
                node = current_node.next
                while node is not None and node.val == current_node.val:
                    node = node.next
                current_node = node

                if prev_node is None:
                    new_head = current_node
                    continue
                else:
                    prev_node.next = current_node
                    continue
            prev_node, current_node = current_node, current_node.next

        return new_head

    # check if the next node has the same value as the current one
    def peek(self, node):
        if node.next is None:
            return False
        return node.next.val == node.val


if __name__ == "__main__":

    head = L.construct_list([1,1,2,2,3,3,3,3])
    L.print_list(Solution().deleteDuplicates(head))
