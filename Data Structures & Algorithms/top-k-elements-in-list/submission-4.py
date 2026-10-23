class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
                
            else:
                d[i]=1
        l=[]
        
        for i in sorted(d.items(), key = lambda x:x[1]):
            l.append(i[0])
        l.reverse()
        return l[:k]