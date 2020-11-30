# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # 生成一个0-len(str)的数组
        list_ori = [i for i in range(len(S) + 1)]
        result = []
        for charater in S:
            if charater == "I":
                result.append(list_ori.pop(0))
            else:
                result.append(list_ori.pop(-1))
        result.append(list_ori[0])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.diStringMatch("DDI"))
