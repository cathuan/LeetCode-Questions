import sys


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print "s=%s, p=%s" % (s, p)

        if len(p) == 0:
            return s == p
        
        if p[-1] != '*':
            if len(s) == 0 or p[-1] != s[-1] and p[-1] != '.':
                return False
            return self.isMatch(s[:-1], p[:-1])

        if len(p) == 1 or p[1] != "*":
            if len(s) == 0:
                return False
            if p[0] == '.' or p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            if self.isMatch(s, p[2:]):
                return True 
            if len(s) == 0:
                return False
            if self.isMatch(s, p[0]+p[2:]):
                return True 
            if (p[0] == '.' or p[0] == s[0]):
                #print s, p
                if self.isMatch(s[1:], p):
                    return True
            return False


if __name__ == "__main__":

    s = sys.argv[1]
    p = sys.argv[2]
    print Solution().isMatch(s, p)