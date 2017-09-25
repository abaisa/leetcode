class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        swapPos = -1
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                swapPos = i
                break
            i -= 1
        if swapPos == -1:
            nums.reverse()
            return
        swapPos2 = swapPos
        for i in range(swapPos, len(nums)):
            if nums[i] < nums[swapPos2] and nums[i] > nums[swapPos-1]:
                swapPos2 = i
        nums[swapPos-1], nums[swapPos2] = nums[swapPos2], nums[swapPos-1]
        l = nums[swapPos:]
        l.sort()
        nums[swapPos:] = l
        return