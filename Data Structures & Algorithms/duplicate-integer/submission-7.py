from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts=Counter(nums)
        if nums == []:
            return False
        for key,val in counts.items():
            if val>1:
                return True
        return False