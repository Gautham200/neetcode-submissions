class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0

        l = 0
        r = len(heights)-1

        while l<r:
            h = min(heights[l],heights[r])

            b = r-l

            area = b*h

            if area>maxx:
                maxx = area
            if heights[l]>heights[r]:
                r=r-1
            else:
                l = l+1
        return maxx