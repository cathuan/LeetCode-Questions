import sys


class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        results = []
        word_map = {}
        for i in range(len(words)):
            word = words[i]
            word_map[word] = i

        for i in range(len(words)):
            word = words[i]
            cur = self.findPalindromePairs(word, i, word_map)
            results.extend(cur)
        return results

    def findPalindromePairs(self, word, index, word_map):
        #print word, index
        results = []
        for i in range(len(word)+1):
            cur = word[:i]
            if cur == cur[::-1]:
                newWord = word[i:][::-1]
                if newWord in word_map and newWord != word:
                    #print cur, word, newWord, index, word_map[newWord]
                    results.append((word_map[newWord], index))

        word = word[::-1]
        for i in range(len(word)+1):
            cur = word[:i]
            if cur == cur[::-1]:
                newWord = word[i:]
                if newWord in word_map and newWord != word:
                    #print cur, word, newWord, index, word_map[newWord]
                    results.append((index, word_map[newWord]))
        return results


if __name__ == '__main__':
    words = ["a", ""]
    print Solution().palindromePairs(words)