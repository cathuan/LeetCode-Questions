from LinkedList import *


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        if head.next is None:
            return head
        if head.next.next is None:
            return head

        first_tail = head
        second_tail = head.next
        while second_tail is not None and second_tail.next is not None:
            first_tail, second_tail = self.process(first_tail, second_tail)

        return head

    def process(self, first_tail, second_tail):

        move_node = second_tail.next
        first_tail.next, second_tail.next, move_node.next = \
            move_node, move_node.next, first_tail.next
        return move_node, second_tail.next


if __name__ == "__main__":

    head = construct_list([0,1,2,3,8,4,6,5])
    print_list(Solution().oddEvenList(head))
