class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and s[i-1]!=" ":
                if count==0:
                    continue
                else:
                    return count
            if s[i]!=" ":
                count+=1
        return count
