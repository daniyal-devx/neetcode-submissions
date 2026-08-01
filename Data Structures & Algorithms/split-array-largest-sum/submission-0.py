class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def canSplit(maxSum: int) -> bool:
            subarrays = 1
            currentSum = 0
            for n in nums:
                if currentSum + n > maxSum:
                    subarrays += 1
                    currentSum = 0
                currentSum += n
            return subarrays <= k

        res = r
        while l <= r:
            maxSum = l + (r - l) // 2
            if canSplit(maxSum):
                res = maxSum
                r = maxSum - 1
            else:
                l = maxSum + 1

        return res