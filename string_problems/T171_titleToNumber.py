# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i, ch in enumerate(s[::-1]):
            res += 26**(i)*(ord(ch)-ord("A")+1 )
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("ZY"))
