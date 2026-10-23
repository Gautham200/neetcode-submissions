class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1

        a = [0]*26
        b = [0]*26

        for i in range(len(s1)):
            a[ord(s1[i])-ord('a')]+=1

        while r<len(s2):
            for i in range(l,r+1):
                b[ord(s2[i])-ord('a')]+=1
            if a == b:
                return True
            b = [0]*26
            r=r+1
            l=l+1
        return False