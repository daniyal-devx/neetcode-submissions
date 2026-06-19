from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        counts=Counter(nums)
        if counts.most_common(1)[0][1]> n/2:
            return counts.most_common(1)[0][0]
        
