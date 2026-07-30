class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity:int):
            needed_days=1
            current=0
            for w in weights:
                if current+w>capacity:
                    needed_days+=1
                    current=0
                current+=w
            return needed_days<=days
        l,r=max(weights),sum(weights)
        while l<r:
            m=l+(r-l)//2
            if canShip(m):
                r=m
            else:
                l=m+1
        return l
            

        