class Solution(object):
    def containsDuplicate(self, nums):
        gap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in gap:
                return True
            gap[num]=i
