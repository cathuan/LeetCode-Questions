class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)
        r = []
        for _ in range(m+1):
            v = []
            for _ in range(n+1):
                v.append(False)
            r.append(v)

        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    if i == 0:
                        r[i][j] = True
                    else:
                        r[i][j] = (s2[:i] == s3[:i])
                elif i == 0:
                    r[i][j] = (s1[:j] == s3[:j])
                else:
                    if r[i-1][j] and s2[i-1] == s3[i+j-1]:
                        r[i][j] = True
                    elif r[i][j-1] and s1[j-1] == s3[i+j-1]:
                        r[i][j] = True
                    else:
                        r[i][j] = False

        return r[m][n]
        

if __name__ == "__main__":

    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbbaccc'
    print Solution().isInterleave(s1, s2, s3)

