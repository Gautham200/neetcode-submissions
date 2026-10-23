class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        c = 0
        for i in nums:
            if i!=0:
                p = p*i
            else:
                c=c+1
        if c>=2:
            return [0]*len(nums)
        l = []
        if c==1:
            for i in nums:
                if i == 0:
                    l.append(p)
                else:
                    l.append(0)
        else:
            for i in nums:
                l.append(int(p/i))
        return l
            
