# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        prev = h
        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return h.next
            tail = curr.next
            curr = prev.next
            a = prev.next
            b = a.next
            c = tail
            for i in range(k):
                a.next = c
                c = a
                a = b
                if i != k-1:
                    b = b.next
            prev.next = c
            prev = curr
'''
链表里面的神坑题！
只可以保证prev和tail之间的元素不空，一定不要越过这个范围（看32行）
处理得当的话，就自然可以应对传进来空表或者交换数位1的情况了
'''