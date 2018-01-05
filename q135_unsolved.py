class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [0]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies.append(candies[-1]+1)
            elif ratings[i] < ratings[i-1]:
                candies.append(candies[-1]-1)
            else:
                candies.append(candies[-1])

        min_candies = min(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + 1 - min_candies

        # more process

        return sum(candies) + len(candies)*(1-min(candies))

    def findTrends(self, nums):

        length = len(nums)
        trends = []
        record_index = 0
        trend = None

        for i in range(1, length):
            if nums[i] == nums[i-1]:
                cur_trend = 0
            elif nums[i] > nums[i-1]:
                cur_trend = 1
            elif nums[i] < nums[i-1]:
                cur_trend = -1

            if trend is None:
                trend = cur_trend
                pass
            elif trend == cur_trend:
                pass
            else:
                if len(trends) == 0 and trend != -1:
                    trends.append((0,-1,0))
                trends.append((record_index, trend, i-1))
                if trend == 1 and cur_trend == -1:
                    trends.append((i-1, 0, i-1))
                record_index = i-1
                trend = cur_trend
        else:
            trends.append((record_index, trend, length-1))
            if trend != 1:
                trends.append((length-1, 1, length-1))

        return trends

    def findPeaks(self, trends):

        peaks = [(0,0)]
        for i in range(1, len(trends)-1):
            start_i, trend, end_i = trends[i]
            if trend != 0:
                continue

            if trends[i-1][1] == 1 and trends[i+1][1] == -1:
                peaks.append((start_i, end_i))
        else:
            start_i, trend, end_i = trends[-1]
            peaks.append((end_i, end_i))
        return peaks

    def modify(self, nums, peaks):





if __name__ == "__main__":

    nums = [1,2,2,3,4,4,4,3,2,1,1,1,0,1]
    trends = Solution().findTrends(nums)
    print trends
    peaks = Solution().findPeaks(trends)
    print peaks
