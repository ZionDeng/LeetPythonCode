# Given an array A of non-negative integers, 
# return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        for i in A:
            if i & 1: # 奇数
                result.append(i)
            else:
                result.insert(0,i)
        return result

        # 用指针：
        # i = 0
        # for j in range(len(A)):
        #     if A[j] % 2 == 0:
        #         A[i], A[j] = A[j], A[i]
        #         i += 1
        # return A



if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([3,1,2,4]))