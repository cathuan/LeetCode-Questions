import bisect

class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        litSeq = []
        for _,h in sorted(envelopes, key = lambda env : (env[0], -env[1])):
            pos = bisect.bisect_left(litSeq, h)
            if pos == len(litSeq):
                litSeq.append(h)
            else:
                litSeq[pos] = h
        return len(litSeq) 