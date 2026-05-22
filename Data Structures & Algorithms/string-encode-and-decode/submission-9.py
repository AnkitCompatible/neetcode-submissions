class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        if strs==[] :
            return "empty"
        for i in range(len(strs)):
            if i == 0:
               encoded=encoded+strs[i] 
            else:
                encoded=encoded+"@*&#"+strs[i]
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=s.split("@*&#")
        if s=="empty":
            return []
        return decoded
