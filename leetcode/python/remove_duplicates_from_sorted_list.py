# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dup = {head.val: True}

        prev = head
        crr = head.next

        while crr:
            if dup.get(crr.val):
                prev.next = crr.next
                crr = prev.next
            else:
                dup[crr.val] = True
                prev = crr
                crr = crr.next

        return head
