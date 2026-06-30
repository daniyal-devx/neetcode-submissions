class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        val=len(nums)//3
        elements=set()
        for n in nums:
            count[n]=count.get(n,0)+1
            if count[n]>val:
                elements.add(n)
        return list(elements)


        
        