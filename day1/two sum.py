class Solution(object):
    def twoSum(self, nums, target):
        gap= {}
        for i in range(len(nums)):
          num= nums[i]
          if (target-num) in gap:
            return [gap[target-num],i]
          gap[num]=i
