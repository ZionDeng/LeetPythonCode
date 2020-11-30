from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # p_odd = 1
        # p_even = 0
        # n = len(A)
        # while p_odd < n and p_even < n:
        #     try:
        #         while A[p_odd] % 2 == 1:
        #             p_odd += 2
        #         while A[p_even] % 2 == 0 :
        #             p_even += 2
        #         A[p_odd], A[p_even] = A[p_even], A[p_odd]
        #     except:
        #         break
        # return A
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParityII([4,6,5,7,4,8,7,3,0,5]))
