class Solution(object):
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
'''
:这个就很有学习意义了，美观且高效
:主要是用了self解决了申请空间的问题，赋值些在一起了
'''