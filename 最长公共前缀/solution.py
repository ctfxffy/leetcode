class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res=""
        if len(strs)==0:
            return ""
        min_len=min(len(strs[i]) for i in range(len(strs)))

  

        for j in range(min_len):
            count=0
            for i in range(1,len(strs)):
                if strs[i][j]!=strs[0][j]:
                    return res
                else:
                    count+=1
            if count==len(strs)-1:
                res+=strs[0][j]
            
        return res
                            