class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for k in range(i+1,len(nums)-2):
                if k>i+1 and nums[k]==nums[k-1]:
                    continue
                l,r=k+1,len(nums)-1
                while l<r:
                    total =nums[i]+nums[l]+nums[k]+nums[r]
                    if total > target:
                        r-=1
                    elif total<target:
                        l+=1
                    else:
                        res.append([nums[i],nums[k],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return res
            
        
        