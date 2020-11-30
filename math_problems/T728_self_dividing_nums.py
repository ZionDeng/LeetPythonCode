from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for numOri in range(left, right + 1):
            digits = []
            num = numOri
            isNum = True
            while num > 0:
                digits.append(num % 10)
                num = num // 10
            if 0 in digits:
                isNum=False
            else:
                for digit in digits:
                    if numOri % digit != 0:
                        isNum = False
            if isNum:
                res.append(numOri)

        return res


s = Solution()
print(s.selfDividingNumbers(1, 22))
