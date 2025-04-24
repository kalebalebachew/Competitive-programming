# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        base = n // k
        extra = n % k
        
        result = [None] * k
        curr = head
        for i in range(k):
            size = base + 1 if extra > 0 else base
            if size == 0:
                result[i] = None
                continue
                
            result[i] = curr
            for j in range(size - 1):
                curr = curr.next
            next_start = curr.next if curr else None
            curr.next = None
            curr = next_start
            
            if extra > 0:
                extra -= 1
        
        return result
        