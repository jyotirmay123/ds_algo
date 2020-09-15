class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n not in a.keys():
                a[nums[i]] = i
            else:
                return [a[n], i]