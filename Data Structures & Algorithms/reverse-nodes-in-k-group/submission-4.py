# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        dummy=ListNode(0,head)
        prev_group_end=dummy
        while True:
            kthnode=self.getkthnode(prev_group_end,k)
            if not kthnode:
                break
            next_group_start=kthnode.next
            prev=next_group_start
            curr=prev_group_end.next
            while curr!=next_group_start:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            temp=prev_group_end.next
            prev_group_end.next=prev
            prev_group_end=temp
        return dummy.next
    def getkthnode(self,node,k):
        curr=node
        for _ in range(k):
            if not curr:
                return None
            curr=curr.next
        return curr
        