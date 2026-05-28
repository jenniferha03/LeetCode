class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in operators and len(stack) >= 2: 
                op2 = stack.pop()
                op1 = stack.pop()
                if i == "+":
                    expr = op1 + op2
                elif i == "-":
                    expr = op1 - op2
                elif i == "*":
                    expr = op1 * op2
                else:
                    expr = int(op1 / op2)
                stack.append(expr)
                expr = 0
            else:
                stack.append(int(i))
        return stack.pop()