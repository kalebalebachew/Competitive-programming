class MinStack:
    def __init__(self):
        self.stack = []  
        self.mn = []  

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mn or val <= self.mn[-1]:
            self.mn.append(val)

    def pop(self) -> None:
        if self.stack and self.stack[-1] == self.mn[-1]:
            self.mn.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.mn[-1] if self.mn else None