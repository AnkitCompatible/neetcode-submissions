class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check={}
        for i in range(len(s)):
            if s[i] in check:
                v=check[s[i]]
                v+=1
                check[s[i]]=v
            else:
                check[s[i]]=1
        for i in range(len(t)):
            if t[i] in check:
                check[t[i]]=check[t[i]]-1
            else:
                return False
        for k in check:
            if check[k] != 0:
                return False
        return True
        