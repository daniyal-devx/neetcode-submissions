# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        i=0
        while curr:
            curr=curr.next
            i+=1
        target = i-n
        if target==0:
            return head.next
        curr=head
        for _ in range(target-1):
            curr=curr.next
        curr.next=curr.next.next

        return head
