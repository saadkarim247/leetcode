class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.track = []

    def push(self, val: int) -> None:
        if (self.min == None or self.min >= val):
            self.min = val
            self.track.append(val)
        self.stack.append(val)

    def pop(self) -> None:
       popped = self.stack.pop()
       if (popped == self.track[-1]):
            self.track.pop()
            if (len(self.track) != 0):
                self.min = self.track[-1]
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.track[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()