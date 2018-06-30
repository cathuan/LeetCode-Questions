import sys


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if s1 == s2:
            return True
        
        if len(s1) != len(s2):
            return False
        
        letters = {}
        seenPartition = False
        isAnalogue = False

        for i in range(len(s1)):
            if isAnalogue:
                seenPartition = True

            char1 = s1[i]
            char2 = s2[i]
            if char1 not in letters:
                letters[char1] = 0
            if char2 not in letters:
                letters[char2] = 0
            letters[char1] += 1
            letters[char2] -= 1
            
            isAnalogue = True
            for char in letters:
                if letters[char] < 0:
                    isAnalogue = False
                    break
            else:
                isAnalogue = True
            
        sameDirection = seenPartition and isAnalogue

        letters = {}
        seenPartition = False
        isAnalogue = False

        for i in range(len(s1)):
            if isAnalogue:
                seenPartition = True

            char1 = s1[i]
            char2 = s2[-1-i]
            if char1 not in letters:
                letters[char1] = 0
            if char2 not in letters:
                letters[char2] = 0
            letters[char1] += 1
            letters[char2] -= 1
            
            isAnalogue = True
            for char in letters:
                if letters[char] < 0:
                    isAnalogue = False
                    break
            else:
                isAnalogue = True
            
        oppoDirection = seenPartition and isAnalogue

        return sameDirection or oppoDirection


if __name__ == '__main__':

    print Solution().isScramble(sys.argv[1], sys.argv[2])