# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list = []
        for i in lists:
            j = i
            if j is not None:
                sorted_list.append(j)
        sorted_list.sort(key=lambda node: node.val)
        head = ListNode(0)
        curr = head
        while sorted_list:
            popOne = sorted_list.pop(0)
            curr.next = popOne
            curr = curr.next
            if popOne.next:
                k = 0
                while k < len(sorted_list):
                    if(sorted_list[k].val > popOne.next.val):
                        break
                    k += 1
                sorted_list.insert(k, popOne.next)
        return head.next
'''
:这里只需要注意一点，删除原lists中的空元素的方法，加了一倍多空间很烦
'''