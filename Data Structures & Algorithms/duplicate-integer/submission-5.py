from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts=Counter(nums)
        if nums == []:
            return False
        if counts.most_common(1)[0][1] > 1 :
            return True 
        return False