class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=[]
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
            else :
                print("true")
                return True
        print("false")
        return False
        