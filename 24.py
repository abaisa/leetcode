# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        a = head
        head = head.next
        b = a.next
        temp = b.next
        b.next = a
        a.next = temp
        prev = a
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            temp = b.next
            b.next = a
            a.next = temp
            prev.next = b
            prev = a
        return head