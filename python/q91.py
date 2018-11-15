class Solution(object):

    def numDecodings(self, s):

        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        results = [1]
        for k in range(1, len(s)+1):
            if k == 1:
                if s[k-1] == '0':
                    results.append(0)
                else:
                    results.append(1)
            else:
                if s[k-1] == "0":
                    if s[k-2] == "0":
                        results.append(0)
                    elif int(s[k-2:k]) <= 26:
                        results.append(results[k-2])
                    else:
                        results.append(0)
                else:
                    if s[k-2] == "0":
                        results.append(results[k-1])
                    elif int(s[k-2:k]) <= 26:
                        results.append(results[k-1] + results[k-2])
                    else:
                        results.append(results[k-1])

        return results[-1]


if __name__ == "__main__":

    print Solution().numDecodings("00000")
