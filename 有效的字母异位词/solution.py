class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False
        
        s_dict={}
        t_dict={}

        for zimu in s :
            if zimu not in s_dict.keys():
                s_dict[zimu]=1
            else :s_dict[zimu]+=1

        for zimu in t :
            if zimu not in t_dict.keys():
                t_dict[zimu]=1
            else :t_dict[zimu]+=1

        if s_dict==t_dict:return True
        else:return False
        