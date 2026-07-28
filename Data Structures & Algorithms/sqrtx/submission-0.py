class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        result =0
        while l<=r:
            mid=(l+r)//2
            res=mid*mid
            if res>x:
                r=mid-1
            elif res<x:
                l=mid+1
                result=mid
            else:
                return mid
        return result
        