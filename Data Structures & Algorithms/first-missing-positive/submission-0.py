class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        i=1
        while count.get(i,0)!=0:
            i+=1
        return i
