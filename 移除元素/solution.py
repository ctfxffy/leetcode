class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        candidate=[]
        k=0
        count=0
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums[i] = -1
                count+=1
                candidate.append(i)
        
        k=len(nums)-count
        for j in range(count):
            nums[candidate[j]],nums[len(nums)-1-j]=nums[len(nums)-1-j],nums[candidate[j]]
           
             
        return k
       