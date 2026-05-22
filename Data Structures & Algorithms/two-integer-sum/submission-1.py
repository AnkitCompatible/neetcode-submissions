class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        find=False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
                    find =True
        if find:
            return output
                
        