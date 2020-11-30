# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        for i in range(1, target):
            for j in range(1, int((2 * target) ** 0.5)+1):
                if sum(range(i, i + j)) == target:
                    result.append(list(range(i, i + j)))
        return result


if __name__ == '__main__':
    s = Solution()
    for i in range(5, 20):
        print(s.findContinuousSequence(i))
