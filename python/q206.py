# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import LinkedList as L


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        if head.next is None:
            return head

        node = head.next
        prev_node = head
        head.next = None
        while node is not None:
            next_node = node.next
            node.next = prev_node
            node, prev_node = next_node, node
        return prev_node


if __name__ == "__main__":

    head = L.construct_list(range(1,10000))
    Solution().reverseList(head)
