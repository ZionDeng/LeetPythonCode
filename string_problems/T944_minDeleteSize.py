from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        for i in zip(*A): # zip 用法
            if list(i) != sorted(i):  # 不能使用is not
                result += 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(['cba','daf','ghi']))