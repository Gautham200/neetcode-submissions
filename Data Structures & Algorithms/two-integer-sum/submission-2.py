class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            r = target - nums[i]
            for j in range(len(nums)):
                
                if j == i:
                    continue
                if nums[j]==r:
                    return [i,j]