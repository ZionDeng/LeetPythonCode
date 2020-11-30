class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        alpha = '0123456789abcdef'
        res = ''
        while num != 0 and len(res) < 8:
            res = alpha[num & 0xf] + res
            num = num >> 4
        return res


s = Solution()
print(16 & 0xffffff)
print(s.toHex(-1))
