class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        avail={}
        for i in range(len(strs)):
            v="".join(sorted(strs[i]))
            if v in avail:
                avail[v].append(i)
            else:
                a=[i]
                avail[v]=a
        output=[]
        print(type(output))
        for k in avail:
            part=[]
            for i in range(len(avail[k])):
                v=avail[k]
                part.append(strs[v[i]])
            output.append(part)
        return output