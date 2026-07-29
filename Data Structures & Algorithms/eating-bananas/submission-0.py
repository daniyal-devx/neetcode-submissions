class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canFinish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h

        res = r
        while l <= r:
            k = l + (r - l) // 2
            if canFinish(k):
                res = k
                r = k - 1
            else:
                l = k + 1

        return res