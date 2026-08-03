# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        def findPeak() -> int:
            l, r = 0, n - 1
            while l < r:
                m = l + (r - l) // 2
                if mountain_arr.get(m) < mountain_arr.get(m + 1):
                    l = m + 1
                else:
                    r = m
            return l

     
        def binarySearch(l: int, r: int, ascending: bool) -> int:
            while l <= r:
                m = l + (r - l) // 2
                val = mountain_arr.get(m)
                if val == target:
                    return m
                if ascending:
                    if val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if val > target:
                        l = m + 1
                    else:
                        r = m - 1
            return -1

        peak = findPeak()

        leftResult = binarySearch(0, peak, True)
        if leftResult != -1:
            return leftResult

        return binarySearch(peak + 1, n - 1, False)