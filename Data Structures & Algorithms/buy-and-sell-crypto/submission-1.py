class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        n=len(prices)
        for r in range(n-1,0,-1):
            l=0
            while l<r:
                profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,profit)
                l+=1
        return maxprofit

        