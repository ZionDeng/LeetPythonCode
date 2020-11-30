# Given an integer n,
#  return a string with n characters such that
# each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters.
#  If there are multiples valid strings, return any of them.  


class Solution:
    def generateTheString(self, n: int) -> str:
        # s = "a"
        # if n % 2 == 0:
        #     for i in range(n - 1):
        #         s += "b"
        # else:
        #     for i in range(n-1):
        #         s += "a"
        # return s

        return "a" * n if n&1 else "a" * (n-1) + "b"


if __name__ == '__main__':
    s = Solution()
    print(s.generateTheString(4))
