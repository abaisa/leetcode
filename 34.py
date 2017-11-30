class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #find a target num
        l, r = 0, len(nums) - 1
        pos = -1
        while l <= r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                pos = m
                break
        if pos == -1:
            return [-1, -1]
        l, r = pos, pos
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums) - 1 and nums[r+1] == target:
            r += 1
        return [l, r]