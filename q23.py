from LinkedList import LinkedList, LinkedNode
import numpy as np


def construct_list_of_nodes(vals):

    nodes = []
    for val in vals:
        node = LinkedNode(val)
        nodes.append(node)

    return nodes


# 232ms. About 13.2%.
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def convert(node):
            if node is None:
                return np.inf
            else:
                return float(node.val)

        start_node = None
        tail_node = None
        current_values = np.array([convert(node) for node in lists])
        if len(current_values) == 0:
            return None

        min_index = current_values.argmin()
        while current_values[min_index] != np.inf:
            node = lists[min_index]
            lists[min_index] = node.next
            current_values[min_index] = convert(node.next)
            node.next = None
            if start_node is None:
                start_node = node
                tail_node = node
            else:
                tail_node.next = node
                tail_node = node
            min_index = current_values.argmin()

        return start_node
