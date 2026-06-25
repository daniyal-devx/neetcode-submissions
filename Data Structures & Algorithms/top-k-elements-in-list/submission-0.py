from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        list =[]
        for i in range(k):
            list.append(counts.most_common()[i][0])
        return list
