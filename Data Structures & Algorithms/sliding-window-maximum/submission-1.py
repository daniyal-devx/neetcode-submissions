class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            curr_max=float('-inf')
            for r in range(i,i+k):
                curr_max=max(curr_max,nums[r])
            res.append(curr_max)
        return res


        