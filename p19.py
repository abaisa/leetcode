# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = head
        back = head
        for i in range(n):
            back = back.next
        if not back:
            return head.next
        while back.next:
            prev = prev.next
            back = back.next
        prev.next = prev.next.next
        return head

'''只需要注意一个点，back向后只和n有关，注意关系，别让back空指针‘’‘