from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        list=[]
        i=len(nums)
        while i >=0:
            for key in hashmap.keys():
                if hashmap[key]==i and k>0:
                    list.append(key)
                    k-=1
                elif k==0:
                    return list
            i-=1
        return list
