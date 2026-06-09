class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in range(len(i)):
                if i[j]==target:
                    return True
        return False