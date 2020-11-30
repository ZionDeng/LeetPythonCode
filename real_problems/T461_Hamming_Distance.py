class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

        # result = 0
        # while y > 0 oxr x > 0:
        #
        #     if x % 2!=y % 2:
        #         result += 1
        #     y = y // 2
        #     x = x // 2
        #
        # return result

        # print(bin(x))
        # print(bin(y))
        # print(bin(x^y))


s = Solution()
print(s.hammingDistance(5, 8))
