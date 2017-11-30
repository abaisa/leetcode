class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        l, r = 0, length - 1
        while l < r:
            m = int((l + r) / 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        rot = l #reverse location
        
        l, r = 0, length - 1
        while l <= r:
            m = (l + r) / 2
            mt = (m + rot) % length
            if nums[mt] < target:
                l = m + 1
            elif nums[mt] > target:
                r = m - 1
            else:
                return mt
        return -1