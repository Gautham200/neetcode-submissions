class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1

        while l<len(numbers) and r>=0:
            t = numbers[l]+numbers[r]

            if t==target:
                return [l+1,r+1]
            elif t<target:
                l=l+1
            else:
                r=r-1
