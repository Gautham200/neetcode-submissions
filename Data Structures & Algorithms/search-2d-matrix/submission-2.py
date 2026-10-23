class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in matrix:
            l, r = 0, len(matrix[0])-1
            if i[r]<target:
                continue
            while l<=r:
                m = (l+r)//2
                if i[m]==target or i[l]==target or i[r]==target: 
                    return True
                if i[m]>target:
                    r = m-1
                else:
                    l = m+1
        return False

