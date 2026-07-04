class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total=m+n
        place=len(nums1)-n
        j=0
        while place < total:
            if j<n:
                nums1[place]=nums2[j]
                j+=1
                place+=1
        nums1.sort()
        
            

        