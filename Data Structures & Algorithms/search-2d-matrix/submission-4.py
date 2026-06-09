class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        block=[]
        for i in matrix:
            if target in i:
                block=i
                break
        if block:
            l,r=0,len(block)-1
            while l<=r:
                c=(l+r)//2
                if block[c]==target:
                    return True
                if block[c]<target:
                    l=c+1
                else:
                    r=c-1
        return False