class Solution:
    def reverseList(self, head):
        """
        The idea is to keeping tracking three pointers
        """

        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev

        return head
