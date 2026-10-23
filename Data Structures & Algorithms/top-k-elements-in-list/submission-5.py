class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]=d[i]+1
        
        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if d[nums[j]]<d[nums[j+1]]:
                    nums[j],nums[j+1] = nums[j+1], nums[j]
        return nums[:k]