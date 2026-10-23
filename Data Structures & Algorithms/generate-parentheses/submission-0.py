class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #s=[]
        res = []

        def func(openn,closen, s=[]):
            if openn>n:
                return
            if openn==closen==n:
                res.append("".join(s))
                return
            if openn<n:
                s.append("(")
                func(openn+1,closen,s)
                s.pop()
            if closen<openn:
                s.append(")")
                func(openn,closen+1,s)
                s.pop()
        func(0,0)
        return res