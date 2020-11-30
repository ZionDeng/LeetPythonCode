class Solution:
    def maximum69Number(self, num: int) -> int:
        filter = [1000, 100, 10,1]
        check=num
        for moder in filter:
            bit = check // moder
            if bit == 9:
                check = check % moder
            elif bit == 6:
                return num + 3 * moder
        return num



s = Solution()
print(s.maximum69Number(9996))
