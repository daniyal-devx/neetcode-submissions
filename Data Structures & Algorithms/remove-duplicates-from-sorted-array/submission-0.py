class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[count]=nums[r]
                count+=1
        return count

        

        