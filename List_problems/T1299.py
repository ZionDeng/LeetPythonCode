from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, num in enumerate(arr):
            maxNum=-1
            for rest in arr[i+1:]:
                if rest > maxNum:
                    maxNum=rest
            arr[i]=maxNum

        return arr


s = Solution()

print(s.replaceElements([17, 18, 5, 4, 6, 1]))
