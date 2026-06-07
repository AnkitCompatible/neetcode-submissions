class Solution:
    def isValid(self, s: str) -> bool:
        # stack=[]
        # for i in range(len(s)):
        #     if s[i]=="[" or s[i]=="(" or s[i]=="{":
        #         stack.append(s[i])
        #     else:
        #         if stack.peek()
        while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
        return s==''