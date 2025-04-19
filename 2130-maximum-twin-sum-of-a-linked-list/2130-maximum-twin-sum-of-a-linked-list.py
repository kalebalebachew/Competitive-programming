# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        v = []
        curr = head
        while curr:
            v.append(curr.val)
            curr = curr.next
        n = len(v)
        mx = 0
        for i in range(n // 2):
            ts = v[i] + v[n-1-i]
            mx = max(mx, ts)
        
        return mx
        