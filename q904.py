class Solution(object):

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) == 0:
            return 0

        fruit1, fruit2 = None, None
        totalFruit1, totalFruit2 = 0, 0
        closeFruit = 0
        maxFruit = -1

        tree.reverse()
        for curFruit in tree:
            if fruit1 is None and fruit2 is None:
                fruit1 = curFruit
                totalFruit1 = 1
                closeFruit = 1
            elif fruit1 is not None and fruit2 is None:
                if curFruit == fruit1:
                    totalFruit1 += 1
                    closeFruit += 1
                else:
                    fruit1, fruit2 = curFruit, fruit1
                    totalFruit1, totalFruit2 = 1, totalFruit1
                    closeFruit = 1
            elif fruit1 is not None and fruit2 is not None:
                if curFruit == fruit1:
                    totalFruit1 += 1
                    closeFruit += 1
                elif curFruit == fruit2:
                    fruit1, fruit2 = fruit2, fruit1
                    totalFruit1, totalFruit2 = totalFruit2+1, totalFruit1
                    closeFruit = 1
                else:
                    fruit1, fruit2 = curFruit, fruit1
                    totalFruit1, totalFruit2 = 1, closeFruit
                    closeFruit = 1
            maxFruit = max(maxFruit, totalFruit1+totalFruit2)
        return maxFruit


if __name__ == "__main__":

    tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print Solution().totalFruit(tree)
