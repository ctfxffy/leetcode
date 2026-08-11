class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s


        index=0
        word_list=[]
        word=""
        for i in range(1,len(s)):
            if s[i-1]==" " and s[i]!=" ":
                index=i
                if index==len(s)-1:
                    word_list.append(s[index])
            elif s[i-1]!=" " and s[i]==" ":
                word_list.append(s[index:i])
            elif s[i-1]!=" " and s[i]!=" " and i==len(s)-1:
                word_list.append(s[index:i+1])
            
        word_list.reverse()
        for i in range(len(word_list)):
            word+=word_list[i]+" "
        return word[:-1]
                
               