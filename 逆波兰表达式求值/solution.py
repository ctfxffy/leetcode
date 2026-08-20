class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        suan_fu=['+','-','*','/']
        stack=[]

        for token in tokens:
            if token not in suan_fu:
                num=int(token)
                stack.append(num)
            else:
                if token==suan_fu[0]:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
                if token==suan_fu[1]:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
                if token==suan_fu[2]:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
                if token==suan_fu[3]:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(float(b) / a))
        return stack[-1]