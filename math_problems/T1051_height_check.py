from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_ori=heights.copy()
        heights.sort()
        result=0
        for i, height in enumerate(heights):

                if height!=heights_ori[i]:

                    result+=1
        return result




s=Solution()
print(s.heightChecker([1,2,3,4,5]))