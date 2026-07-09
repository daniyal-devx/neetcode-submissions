class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        i,j=0,len(heights)-1
        while i < j:
            min_h=min(heights[i],heights[j])
            width=j-i
            area=width*min_h
            if area>max:
                max=area
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max
        