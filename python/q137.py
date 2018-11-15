
# 6.8%. Slow. I think it's because we loop over the list too many times.
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_num = max(nums)
        min_num = min(nums)
        max_abs = max(abs(max_num), abs(min_num))

        mask = 1
        answer = 0
        sign = None
        while mask <= max_abs:
            count = sum([1*(1 if num > 0 else -1) for num in nums if abs(num)&mask != 0])
            if count % 3 != 0:
                if sign is None:
                    sign = 1 if count % 3 == 1 else -1
                answer += mask*sign
            mask *= 2
        return answer

        int count = 0;
  while(n != 0) {
    count++;
    n=n&(n-1);
  }
  return count;



if __name__ == "__main__":

    nums = list(range(100000,10000000))*3
    nums.append(-5)
    print(Solution().singleNumber(nums))
