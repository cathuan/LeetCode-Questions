class Solution(object):

    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """

        numCity = len(flights)
        numWeeks = len(days[0])

        # dp[i][j]: i = days, j = city
        dp = []
        for _ in range(numWeeks):
            dp.append([0]*numCity)

        for city in range(numCity):
            dp[numWeeks-1][city] = days[city][numWeeks-1]

        for day in range(numWeeks-2,-1,-1):
            for city in range(numCity):
                maxDay = 0
                for nextCity in range(numCity):
                    if flights[city][nextCity] == 1 or nextCity == city:
                        maxDay = max(maxDay, dp[day+1][nextCity])
                dp[day][city] = maxDay + days[city][day]

        ret = 0
        for city in range(numCity):
            if flights[0][city] == 1 or city == 0:
                ret = max(ret, dp[0][city])
        return ret


if __name__ == "__main__":
    flights = [[0,1,1],[1,0,1],[1,1,0]]
    days = [[1,3,1],[6,0,3],[3,3,3]]
    print Solution().maxVacationDays(flights, days)