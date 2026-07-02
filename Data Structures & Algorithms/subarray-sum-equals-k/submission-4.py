class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixcount={0:1}
        currentsum=0
        count=0
        for n in nums:
            currentsum+=n
            count+=prefixcount.get(currentsum-k,0)
            prefixcount[currentsum]=prefixcount.get(currentsum,0)+1
        return count



        