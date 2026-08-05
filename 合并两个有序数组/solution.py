class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return
        for i in range(n):
            nums1[m+i] = nums2[i]

        for i in range(m+n):
            min_index=i
            for j in range(i+1,m+n):
                if nums1[j]<nums1[min_index]:
                    min_index=j
            nums1[i],nums1[min_index]=nums1[min_index],nums1[i]
            