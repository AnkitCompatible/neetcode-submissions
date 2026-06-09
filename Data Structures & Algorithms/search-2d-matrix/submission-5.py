class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        block=[]
        for i in matrix:
            if target in i:
                block=i
        if block:
            for i in block:
                if i==target:
                    return True
        return False