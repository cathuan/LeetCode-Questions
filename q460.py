class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.frequency = 0
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.sentinal = Node()
        self.sentinal.prev = self.sentinal
        self.sentinal.next = self.sentinal
        self.length = 0

    def push(self, node):
        self.length += 1
        tail = self.sentinal.prev
        self.sentinal.prev = node
        node.next = self.sentinal
        node.prev = tail
        tail.next = node

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        tail = self.sentinal.prev
        self.sentinal.prev = tail.prev
        tail.prev.next = self.sentinal
        return tail

    def popleft(self):
        if self.length == 0:
            return None
        self.length -= 1
        head = self.sentinal.next
        self.sentinal.next = head.next
        head.next.prev = self.sentinal
        return head

    def delete(self, node):
        self.length -= 1
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.freqs = {}  # freq -> DoublyLinkedList(capacity)
        self.values = {}  # key -> node
        self.min_freq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.values:
            node = self.values[key]
            assert node.key == key
            self.freqs[node.frequency].delete(node)
            if self.freqs[node.frequency].length == 0:
                del self.freqs[node.frequency]
            node.frequency += 1
            self.min_freq = min(self.min_freq, node.frequency)
            if node.frequency not in self.freqs:
                self.freqs[node.frequency] = DoublyLinkedList()
            self.freqs[node.frequency].push(node)
            return node.val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.values:
            node = self.values[key]
            self.freqs[node.frequency].delete(node)
            if self.freqs[node.frequency].length == 0:
                del self.freqs[node.frequency]
                self.min_freq += 1
            node.frequency += 1
            node.val = value
            if node.frequency not in self.freqs:
                self.freqs[node.frequency] = DoublyLinkedList()
            self.freqs[node.frequency].push(node)
        else:
            if self.capacity == 0:
                return

            # pop the least used node from cache
            if len(self.values) > self.capacity:
                poped_node = self.freqs[self.min_freq].popleft()
                if poped_node is not None:
                    del self.values[poped_node.key]
                if self.freqs[self.min_freq] == 0:
                    del self.freqs[self.min_freq]

            node = Node(key, value)
            self.values[key] = node
            node.frequency = 1
            self.min_freq = 1
            if node.frequency not in self.freqs:
                self.freqs[node.frequency] = DoublyLinkedList()
            self.freqs[node.frequency].push(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
