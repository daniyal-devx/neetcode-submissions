class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            curr = head
            while curr:
                values.append(curr.val)
                curr = curr.next
        
        values.sort()
        dummy = ListNode()
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next