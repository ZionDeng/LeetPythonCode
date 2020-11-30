# 查找常用字符
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # result = []
        # words = [list(i) for i in A]
        # target = A.pop()
        # for letter in target:
        #     is_common = True
        #     for word in words:
        #         if word.count(letter) == 0:
        #             is_common = False  # 如果不存在则不是
        #         else:
        #             word.remove(letter)  # 如果是共同的就先去除掉
        #     if is_common:
        #         result.append(letter)
        # return result
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)  # 找出每个单词里面这个字母出现的次数
            res += minnum*k  # 按最小的放到result里面
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.commonChars(["cool", "lock", "cook"]))
