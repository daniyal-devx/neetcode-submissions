class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        def canSplit(maxsum:int) -> bool:
            subarrays=1
            current_sum=0
            for n in nums:
                if current_sum+n>maxsum:
                    subarrays+=1
                    current_sum=0
                current_sum+=n
            return subarrays<=k
        res=r
        while l<=r:
            m=l+(r-l)//2
            if canSplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        