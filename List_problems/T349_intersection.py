from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result += [i]
        return result
        # return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5], [9,4,9,8,4]))
