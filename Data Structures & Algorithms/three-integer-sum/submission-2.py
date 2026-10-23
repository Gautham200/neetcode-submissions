class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        i=0
        l=i+1
        r=len(nums)-1

        res=[]
        if nums == [0,0,0]:
            return [[0,0,0]]

        while i<=len(nums)-3:
            l=i+1
            r=len(nums)-1
            if i>0:
                if nums[i]==nums[i-1]:
                    i=i+1
                    continue
            while l<len(nums)-1 and r>=0 and l<r:
                t = nums[i]+nums[l]+nums[r]
                if t == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                if t<0:
                    l=l+1
                else:
                    r=r-1
            i=i+1
        return res