class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        
        popped = self.stack.pop()
        
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        
        return popped

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        temp = self.min_stack[-1]
        self.min_stack.pop()
        return temp


a = MinStack()

a.push(452)
a.push(a25)
a.push(65)
a.push(43)
print(a.getMin())
print(a.getMin())
print(a.getMin())
print(a.getMin())
print(a.getMin())
print(a.getMin())
print(a.getMin())
