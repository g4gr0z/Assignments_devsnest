class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return [0]*len(nums)
	#when no. of zero is 0
        if nums.count(0)<1:
            arr=[]
            ans=1
            for i in nums:
                ans*=i
            for i in range(len(nums)):
                arr.append(ans//nums[i])
            return arr
	#when no. of zero is 1
        else:
            arr=[]
            ans=1
            for i in nums:
                if i!=0:
                    ans*=i
            for i in range(len(nums)):
                if nums[i]!=0:
                    arr.append(0)
                else:
                    arr.append(ans)
            return arr
