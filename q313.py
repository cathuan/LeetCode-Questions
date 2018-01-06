
# 92.05% 422ms
class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        ugly_numbers = [1]
        n_primes = len(primes)
        indices = [0] * n_primes
        new_generated_nums = primes[:]  # copy the primes list

        while len(ugly_numbers) != n:
            min_value = min(new_generated_nums)  # when the size is small, list is faster than ndarray
            ugly_numbers.append(min_value)

            for i in xrange(n_primes):
                if min_value == new_generated_nums[i]:
                    indices[i] += 1
                    new_generated_nums[i] = ugly_numbers[indices[i]] * primes[i]

        return ugly_numbers[-1]


# 46.59% 882ms
class Solution2(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        ugly_numbers = [1]
        n_primes = len(primes)
        indices = [0] * n_primes

        while len(ugly_numbers) != n:
            new_generated_nums = [ugly_numbers[indices[i]]*primes[i] for i in xrange(n_primes)]
            min_value = min(new_generated_nums)

            for i in xrange(n_primes):
                if min_value == new_generated_nums[i]:
                    indices[i] += 1

            ugly_numbers.append(min_value)

        return ugly_numbers[-1]


if __name__ == "__main__":

    n = 12
    primes = [2,7,13,19]

    print Solution().nthSuperUglyNumber(n, primes)
    print Solution2().nthSuperUglyNumber(n, primes)
