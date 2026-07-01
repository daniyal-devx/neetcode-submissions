class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixcount={0:1}
        currentsum=0
        count=0
        for n in nums:
            currentsum+=n
            if currentsum-k in prefixcount:
                count+=prefixcount[currentsum-k]
            prefixcount[currentsum]=prefixcount.get(currentsum,0)+1
        return count



        