class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')

    def push(self, val: int) -> None:
        self.stack.append([val, self.min_num])
        self.min_num = min(self.min_num, val) 

    def pop(self) -> None:
        self.min_num = self.stack[-1][-1]
        del self.stack[-1]

    def top(self) -> int:
        top_stack = self.stack[-1][0]
        return top_stack

    def getMin(self) -> int:
        return self.min_num
                
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()