class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        s = []
        l = []

        def evaluate(b, a, o):
            if o == '+':
                return int(a) + int(b)
            elif o == '-':
                return int(a) - int(b)
            elif o == '/':
                return int(a) / int(b)
            elif o == '*':
                return int(a) * int(b)

        for i in tokens:
            if i == '+' or i == '*':
                a = s.pop()
                b = s.pop()
                v = evaluate(int(a), int(b), i)
                s.append(v)
            elif i == '-':
                a = s.pop()
                b = s.pop()
                v = evaluate(int(a), int(b), i)
                s.append(v)
            elif i == '/':
                a = s.pop()
                b = s.pop()
                v = evaluate(int(a), int(b), i)
                s.append(v)
            else:
                s.append(int(i))
        return int(s[-1])
            
        