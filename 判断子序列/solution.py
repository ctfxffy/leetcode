class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False
    
        i=0
        j=0
        while j<len(t):

            if i==len(s):
                return True
            if s[i]==t[j]:
                i=i+1
            j=j+1
        
        if i==len(s):
            return True
        else: return False