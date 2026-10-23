class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0

        l , r = 0, 0
        c = 0
        while r<len(s) and l<=r:
            while s[r] in s[l:r] and l<=r:
                c=c-1
                l=l+1
            c=c+1
            if c>m:
                m=c
            r=r+1
        return m
            
            