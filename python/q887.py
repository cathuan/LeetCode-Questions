class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        buf = [0]*K
        t = 1
        while True:
            newBuf = [0] * K
            for k in range(K):
                if k == 0:
                    value = t
                elif t == 1:
                    value = 1
                else:
                    value = buf[k-1] + buf[k] + 1
                if value >= N:
                    return t
                newBuf[k] = value
            buf = newBuf
            t += 1


if __name__ == "__main__":
    k = 3
    n = 14
    print Solution().superEggDrop(k, n)
