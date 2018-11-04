class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.sentinal = Node()
        self.sentinal.prev = self.sentinal
        self.sentinal.next = self.sentinal
        self.length = 0

    def push(self, key, val):
        self.length += 1
        node = Node(key, val)
        tail = self.sentinal.prev
        self.sentinal.prev = node
        node.next = self.sentinal
        node.prev = tail
        tail.next = node
        return node

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


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = capacity
        self.values = DoublyLinkedList()
        self.values_dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.values_dict:
            node = self.values_dict[key]
            assert node.key == key
            self.values.delete(node)
            new_node = self.values.push(key, node.val)
            self.values_dict[key] = new_node
            return new_node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.values_dict:
            node = self.values_dict[key]
            assert node.key == key
            self.values.delete(node)
            new_node = self.values.push(key, value)
            self.values_dict[key] = new_node
        else:
            if self.values.length == self.capacity:
                poped_node = self.values.popleft()
                del self.values_dict[poped_node.key]
            new_node = self.values.push(key, value)
            self.values_dict[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
