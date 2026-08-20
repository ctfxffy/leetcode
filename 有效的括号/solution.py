class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        paris={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            else:
                if not stack or stack[-1]!=paris[ch]:
                    return False
                stack.pop()
        
        return not stack