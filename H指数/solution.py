class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i in range(len(citations)):
            min_index=i
            for j in range(i,len(citations)):
                if citations[j]<citations[min_index]:
                    min_index=j
            citations[i],citations[min_index]=citations[min_index],citations[i]

        res=[]
        
        for h in range(1,len(citations)+1):
            if citations[len(citations)-h]>=h:
                res.append(h)
       
        if len(res)==0:
            return 0

        return max(res)