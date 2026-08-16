class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in lookup:
                return [lookup[need], i]

            lookup[nums[i]] = i
