class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        cur_sum = 0
        ans = float("inf")

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans