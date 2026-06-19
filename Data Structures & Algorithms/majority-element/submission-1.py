
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total=len(nums)
        hashmap={}
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
            if hashmap[n]>total/2:
                return n
        
        
