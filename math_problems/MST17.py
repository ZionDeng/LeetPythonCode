from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result = []
        for i in range(1,(10 ** n)):
            result.append(i)
        return result


solution = Solution()
print(solution.printNumbers(3)[-1])
