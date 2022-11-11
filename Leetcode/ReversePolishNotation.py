class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        operators = {'*': lambda x, y: x * y,
                     '+': lambda x, y: x + y,
                     '/': lambda x, y: x / y,
                     '-': lambda x, y: x - y}
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                
                ans = int(operators[i](int(stack[len(stack) - 2]),int(stack[len(stack) - 1])))
                stack.pop()
                stack.pop()
                stack.append(ans)
        return stack[0]
