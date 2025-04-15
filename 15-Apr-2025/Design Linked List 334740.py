# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head
        for i in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1
    
    def addAtHead(self, val: int) -> None:
        nn = ListNode(val)
        nn.next = self.head
        self.head = nn
    
    def addAtTail(self, val: int) -> None:
        nn = ListNode(val)
        if not self.head:
            self.head = nn
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nn
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        nn = ListNode(val)
        curr = self.head
        for i in range(index - 1):
            if not curr:
                return
            curr = curr.next
        if not curr:
            return
        nn.next = curr.next
        curr.next = nn
    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        if index == 0 and self.head:
            self.head = self.head.next
            return
        curr = self.head
        for i in range(index - 1):
            if not curr:
                return
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next