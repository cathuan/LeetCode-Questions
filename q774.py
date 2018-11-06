class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """

        distances = []
        for i in range(len(stations)-1):
            distances.append(stations[i+1] - stations[i])

        minD = 0
        maxD = 10000*10000
        while maxD - minD > 1e-6:
            mid = (minD + maxD)*1.0/2
            if self.isPossible(distances, mid, K):
                maxD = mid
            else:
                minD = mid
        return (maxD+minD)*1.0/2

    def isPossible(self, distances, D, K):
        requiredStations = 0
        for distance in distances:
            requiredStations += int(distance / D)
        return requiredStations <= K


if __name__ == "__main__":

    print Solution().minmaxGasDist([1,2,3,4,5,6,7,8,9,10], 10)