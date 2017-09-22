class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        flag = 0
        prev = None
        for i in nums:
            if prev != i:
                nums[flag] = i
                res += 1
                flag += 1
            prev = i
        return res