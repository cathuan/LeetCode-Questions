# XXX: Stop as early as possible.

class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        df={}
        return self.helper(s, len(s), df, wordDict)

    def helper(self, s, i, df, wordDict):
        #print i, df
        if i in df:
            return df[i]
        if s[:i] in wordDict:
            results=[s[:i]]
        else:
            results=[]
        for j in range(1,i):
            if s[j:i] in wordDict:
                tmp = self.helper(s, j, df, wordDict)
                for st in tmp:
                    results.append(st+" "+s[j:i])
        df[i]=results
        return results


if __name__ == "__main__":

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print Solution().wordBreak(s, wordDict)
