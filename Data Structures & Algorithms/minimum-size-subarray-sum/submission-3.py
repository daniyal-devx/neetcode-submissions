class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minf = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minf = min(minf, r - l + 1)
                total -= nums[l]
                l += 1

        return minf if minf != float('inf') else 0