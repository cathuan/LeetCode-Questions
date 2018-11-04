import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []  # [value]
        self.indices = {}  # value -> set([index])
        

    # append val at the end of self.values to keep a record
    # add the index of the newly added val in self.indices so it's easier to get an index of the value when we need
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.indices:
            self.indices[val] = set()
            ret = False
        else:
            ret = True
        self.indices[val].add(len(self.values))
        self.values.append(val)
        return ret

    # Randomly pick an index from self.indices[val]. If the index is actually the end of the self.values, remove it; otherwise, swap
    # the last element of self.values with index.
    # Remember to swap the index of the last element in self.indices. This is the reason why we use set() in self.indices, since
    # it's easier to remove/add elements from a set (O(1) in average)
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.indices:
            return False

        indices = self.indices[val]
        index = indices.pop()
        if index == len(self.values) - 1:
            self.values.pop()
        else:
            value = self.values.pop()
            self.values[index] = value
            self.indices[value].remove(len(self.values))
            self.indices[value].add(index)
        if not self.indices[val]:
            del self.indices[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """

        index = random.randint(0, len(self.values)-1)
        return self.values[index]


if __name__ == "__main__":

    #["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    #[[],[10],[10],[20],[20],[30],[30],[10],[10],[30],[30],[],[],[],[],[],[],[],[],[],[]]

    r = RandomizedCollection()
    r.insert(10)
    r.insert(10)
    r.insert(20)
    r.insert(20)
    r.insert(30)
    r.insert(30)
    r.remove(10)
    r.remove(10)
    r.remove(30)
    r.remove(30)