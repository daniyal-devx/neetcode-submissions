class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        for i in range(len(nums)):
            rightprod=1
            for j in range(i):
                output[i]*=nums[j]
            for m in range(i+1,len(nums)):
                rightprod*=nums[m]
            output[i]*=rightprod
        return output

           