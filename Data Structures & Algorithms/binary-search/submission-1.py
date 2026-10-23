class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        while l+1<r:
            m = (l+r)//2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            if nums[m] == target:
                return m
            if nums[m]>target:
                r = m
            else:
                l = m
        return -1