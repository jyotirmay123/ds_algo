class Solution:
    def twoSum(self, nums, target):
        valList = []
        for i, val in enumerate(nums):
            if val in valList:
                return [valList.index(val), i]
            else:
                more = target - val
                valList.append(more)
