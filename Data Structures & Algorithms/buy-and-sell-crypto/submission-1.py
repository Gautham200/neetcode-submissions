class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        m = 0

        l, r = 0, 1
        lm, rm = prices[0],0
        while r<len(prices) and l<r:
            if (prices[r]-prices[l])>m:
                m = prices[r]-prices[l]
            if lm>prices[r]:
                l=r
                lm = prices[l]
            r = r+1
        return m