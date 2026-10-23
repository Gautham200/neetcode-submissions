class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            elif len(l)==0:
                return False
            elif i == ')':
                t=l.pop()
                if t!='(':
                    return False
            elif i == '}':
                t=l.pop()
                if t!='{':
                    return False
            elif i == ']':
                t=l.pop()
                if t!='[':
                    return False
        if len(l)==0:
            return True
        return False