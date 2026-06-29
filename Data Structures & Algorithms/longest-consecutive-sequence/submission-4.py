class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        maxcount=0
        totalset=set(nums)
        for num in totalset:
            if num-1 not in totalset:
                count=1
                while num+1 in totalset:
                     num+=1
                     count+=1
                if count>maxcount:
                    maxcount=count
        return maxcount
        