class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def eval(a,b,op):
            if op == '+':
                return int(a)+int(b)
            elif op == '-':
                return int(a)-int(b)
            elif op == '/':
                return int(a)/int(b)
            else:
                return int(a)*int(b)
        s = []

        for i in tokens:
            if i.isnumeric() or len(i)>1:
                s.append(i)
            else:
                a = s.pop()
                b = s.pop()
                v = eval(b, a, i)
                s.append(v)
            
        return int(s[0])
            
        