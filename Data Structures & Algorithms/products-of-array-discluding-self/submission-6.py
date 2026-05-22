class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        output=[]
        for i in range(len(nums)):
            mul*=nums[i]
        count=0
        if mul==0:
            for i in range(len(nums)):
                if nums[i]==0:
                    count+=1
                    continue
                if mul==0:
                    mul=1
                mul*=nums[i]
                print(mul)
            for i in range(len(nums)):
                if nums[i]==0 :
                    output.append(mul)
                    continue
                output.append(0)
        else:
            for i in range(len(nums)):
                output.append(mul//nums[i])
        if count >1:
            return [0]*len(output)
        return output