# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        if self.count == 0:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        if self.count == 0:
            self.front = -1
            self.rear = -1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size