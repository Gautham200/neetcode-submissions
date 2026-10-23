class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = nums[l]
        
        while l<r:
            mid = (l+r)//2
            if nums[l]<m:
                m = nums[l]
            elif nums[r]<m:
                m = nums[r]
            if nums[mid]<m:
                m = nums[mid]
            if nums[r]<nums[mid]:
                l = mid+1
            else :
                r = mid-1
        return m