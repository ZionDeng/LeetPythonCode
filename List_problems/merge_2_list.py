# https://leetcode-cn.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        :type: nums1: List[int], size = m+n
        :type: nums2: List[int], size = n
        rtype: None 
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort()
        # return nums1
        p  = m + n -1 
        m -= 1 
        n -= 1 
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[p] = nums1[m]
                m -= 1 
            else: 
                nums1[p] = nums2[n]
                n -= 1 
            p -= 1 
        while n >= 0:
            nums1[p] = nums2[n]
            p -= 1
            n -= 1 
