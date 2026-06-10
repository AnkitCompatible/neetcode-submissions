class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        banana=r
        while l<=r:
            mid=(l+r)//2
            totalT=0
            for i in piles:
                totalT+=math.ceil(i/mid)
            if totalT<=h:
                banana=mid
                r=mid-1
            else:
                l=mid+1
        return banana
        

