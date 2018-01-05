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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        nodes = []
        current_node = head
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next

        index = len(nodes) - n
        if index == 0:
            if len(nodes) == 1:
                return None
            else:
                return nodes[1]
        elif index == len(nodes) - 1:
            nodes[index-1].next = None
        else:
            nodes[index-1].next = nodes[index+1]
        return head


if __name__ == "__main__":

    head = construct_list([1,2,3])
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 3)
    print_list(new_head)
