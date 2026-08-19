class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0


        candidate=[]
        nums.sort()
        cnt=1
        for i in range (1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            if nums[i-1]==nums[i]-1:
                cnt+=1
            else :
                candidate.append(cnt)
                cnt=1
            
        if len(candidate)==0:
            return cnt
        else:return max(cnt,max(candidate))