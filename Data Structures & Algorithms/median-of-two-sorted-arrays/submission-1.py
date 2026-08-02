class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Number of elements on the left side
        
        left, right = 0, m
        
        while left <= right:
            # Partition positions
            partition1 = (left + right) // 2
            partition2 = half - partition1
            
            # Handle edge cases where partition is at the boundaries
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found the correct partition
                if total % 2 == 0:
                    # Even length: average of two middle elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # Odd length: max of left elements
                    return max(maxLeft1, maxLeft2)
            
            elif maxLeft1 > minRight2:
                # Too many elements from nums1 on the left, move partition left
                right = partition1 - 1
            else:
                # Too few elements from nums1 on the left, move partition right
                left = partition1 + 1
        
        # Should never reach here for valid input
        return -1