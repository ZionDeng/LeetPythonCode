from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in  range(0,len(nums),2):
            for _ in range(nums[i]):
                result.append(nums[i+1])

        return result


solution = Solution()
input = [1,2,3,4]
print(solution.decompressRLElist(input))
