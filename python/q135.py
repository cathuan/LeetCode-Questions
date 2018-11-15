class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies.append(candies[i-1]+1)
            else:
                candies.append(1)

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)


if __name__ == "__main__":

    ratings = [12,4,3,11,34,34,1,67]
    print Solution().candy(ratings)
