import LinkedList as L


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head

        prev_node = None
        node = head
        count = 1
        while count < m:
            count += 1
            prev_node = node
            node = node.next
        node = self.reverseList(node, m, n)
        if prev_node is None:
            return node
        else:
            prev_node.next = node
            return head

    def reverseList(self, head, m, n):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head.next
        prev_node = head
        count = 2
        while count <= n - m + 1:
            count += 1
            next_node = node.next
            node.next = prev_node
            node, prev_node = next_node, node

        head.next = node
        return prev_node


if __name__ == "__main__":

    head = L.construct_list(range(1,11))
    L.print_list(Solution().reverseBetween(head,3,8))
