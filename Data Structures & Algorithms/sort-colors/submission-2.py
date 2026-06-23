
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        j=0
        for n in [0,1,2]:
            while hashmap.get(n,0)>=1:
                nums[j]=n
                hashmap[n]-=1
                j+=1


            
      
        