class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        minn = r
        while l<=r:
            m = (l+r)//2
            s = 0
            for i in piles:
                s = s+math.ceil(i/m)
            if s<=h:
                r = m-1
                if m<=minn:
                    minn = m
            else:
                l = m+1
            
        return minn
