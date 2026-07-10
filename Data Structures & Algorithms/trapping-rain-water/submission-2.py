class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        suffix=[0]*n
        prefix=[0]*n
        area=0
        for i in range(n):
            maxprefix=0
            l=0
            while l<=i:
                maxprefix=max(maxprefix,height[l])
                l+=1
            prefix[i]=maxprefix
        for i in range(n):
            maxsuffix=0
            r=len(height)-1
            while r>=i:
                maxsuffix=max(maxsuffix,height[r])
                r-=1
            suffix[i]=maxsuffix
        for i in range(n):
            area+=min(prefix[i],suffix[i])-height[i]
        return area
            
        