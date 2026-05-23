class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict={}
        for i in range(len(nums)):
            if nums[i] in newdict:
                newdict[nums[i]]+=1
            else:
                newdict[nums[i]]=1
        freq=[]
        output=[]
        for key in newdict:
            freq.append(newdict[key])
        freq.sort(reverse="True")
        print(freq)
        for i in range(k):
            for key in newdict:
                if newdict[key]==freq[i] and key not in output:
                    output.append(key)
            print(output)
        return output