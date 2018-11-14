from collections import namedtuple

Record = namedtuple("Record", ["pos", "neg"])


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        records = []
        records.append(Record(None, None))

        for num in nums:
            r = records[-1]
            newRecord = self.getNew(r, num)
            records.append(newRecord)
        
        r = records[-1]
        if r.pos is None:
            records.append(Record(r.neg, r.pos))

        maxValue = float("-inf")
        for r in records[1:]:
            if r.pos is not None:
                maxValue = max(maxValue, r.pos)
        return maxValue

    def getNew(self, oldRecord, num):

        if num == 0:
            return Record(0, 0)
        elif num > 0:
            if oldRecord.pos == 0 or oldRecord.pos is None:
                pos = num
            else:
                pos = oldRecord.pos * num

            neg = oldRecord.neg * num if oldRecord.neg is not None else None
            return Record(pos, neg)
        else:
            if oldRecord.pos == 0 or oldRecord.pos is None:
                neg = num
            else:
                neg = oldRecord.pos * num

            pos = oldRecord.neg * num if oldRecord.neg is not None else None
            return Record(pos, neg)


if __name__ == "__main__":

    nums = [-2]
    print Solution().maxProduct(nums)
