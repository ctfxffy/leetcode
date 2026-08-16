class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup and i - lookup[nums[i]] <= k:
                return True
            lookup[nums[i]] = i

        return False