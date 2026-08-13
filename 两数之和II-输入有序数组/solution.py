class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        i=0
        j=len(numbers)-1

        while i<j:
            if numbers[i]+numbers[j]<target:
                i=i+1
            if numbers[i]+numbers[j]>target:
                j=j-1
            if numbers[i]+numbers[j]==target:
                index.append(i+1)
                index.append(j+1)
                return index