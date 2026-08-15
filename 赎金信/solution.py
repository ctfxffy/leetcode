class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lookup = {}
        for i in range(len(magazine)):
            if magazine[i] not in lookup:
                lookup[magazine[i]] = 1
            else:
                lookup[magazine[i]] += 1


        for i in range(len(ransomNote)):
            if ransomNote[i] in lookup and lookup[ransomNote[i]] != 0:
                lookup[ransomNote[i]] -= 1
            elif ransomNote[i] not in lookup or lookup[ransomNote[i]] == 0:
                return False

        return True
