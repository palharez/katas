# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1, head2):
        return self.merge_lists(head1, head2)

    def merge_lists(self, head1, head2):
        temp = None

        if head1 is None:
            return head2

        if head2 is None:
            return head1

        if head1.val <= head2.val:
            temp = head1

            temp.next = self.merge_lists(head1.next, head2)

        else:
            temp = head2

            temp.next = self.merge_lists(head1, head2.next)

        return temp
