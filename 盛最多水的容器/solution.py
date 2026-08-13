class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_ans=0
        while left<right:
            ans=(right-left)*min(height[left],height[right])
            if ans>max_ans:
                max_ans=ans
            
            if(height[left]<height[right]):
                left+=1
            else:right-=1

        return max_ans


