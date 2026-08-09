# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        lastprev,curr=dummy,head
        for _ in range(left-1):
            lastprev=curr
            curr=curr.next
        prev =None
        for _ in range(right-left+1):
            tmpnext=curr.next
            curr.next=prev
            prev,curr=curr,tmpnext
        lastprev.next.next=curr
        lastprev.next=prev
        return dummy.next

