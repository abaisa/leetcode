class Solution(object):
    def fourSum(self, nums, target):
        if len(nums)<=3:
            return []
        sums = {} #a dictionary.
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] not in sums:
                    sums[nums[i]+nums[j]]=[[i,j]]
                else:
                    sums[nums[i]+nums[j]].append([i,j])
        print(sums)
        ans = set()
        checked = set()
        for x in sums:
            if target-x in sums and x not in checked:
                for elements in sums[x]: #pair 
                    [i1,j1] = elements[0],elements[1]
                    for items in sums[target-x]:
                        if i1 not in items and j1 not in items:
                            possible = sorted([nums[i1],nums[j1],nums[items[0]],nums[items[1]]])
                            possible = tuple(possible)
                            ans.add(possible)
            checked.add(target-x)
        return [list(answer) for answer in ans]
#这个写法比较奇特，先统计了一个两个数相加的字典，之后再进行一系列的计算。效率比自己写的暴力方法要好，但是还有一些改进空间。