class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t={}
        t_to_s={}
        for i in range(len(s)):
            if s[i] not in s_to_t.keys():
                s_to_t[s[i]]=t[i]
            if t[i] not in t_to_s.keys():
                t_to_s[t[i]]=s[i]
            if s[i] in s_to_t.keys() and s_to_t[s[i]]!=t[i]:
                return False
            if t[i] in t_to_s.keys() and t_to_s[t[i]]!=s[i]:
                return False
        return True