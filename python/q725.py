from LinkedList import *


# 97.83%. Sort of boring question.. Would expect there are nontrivial solution.
class Solution(object):

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        length = self.countLength(root)
        partitions = self.calPartitionNumbers(length, k)
        results = []
        next_head = root
        for partition in partitions:
            head, next_head = self.splitList(next_head, partition)
            results.append(head)
        return results

    def countLength(self, root):
        length = 0
        node = root
        while node is not None:
            length += 1
            node = node.next
        return length

    def calPartitionNumbers(self, length, k):

        part = length // k
        remainder = length % k
        partitions = [part] * k
        for i in range(remainder):
            partitions[i] += 1
        return partitions

    def splitList(self, root, partition):
        if partition == 0:
            return None, None
        else:
            count = 1
            node = root
            while count < partition:
                count += 1
                node = node.next
            next_root = node.next
            node.next = None
            return root, next_root


if __name__ == "__main__":

    root = construct_list(range(10))
    k = 3
    split = Solution().splitListToParts(root, k)
    for head in split:
        print_list(head)
