class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max=[-1]*len(height)
        right_max=[-1]*len(height)
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i+1])

        sum=0
        for i in range(len(height)):
            if(min(left_max[i],right_max[i])>height[i]):
                sum+=min(left_max[i],right_max[i])-height[i]
        return sum