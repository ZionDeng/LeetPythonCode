class Solution:
    def balancedStringSplit(self, s: str) -> int:

        # if len(s) <= 0 or s == '':
        #     return 0
        # numFirst, numSecond, index = 1, 0, 1
        # while numFirst != numSecond:
        #     if s[index] == s[0]:
        #         numFirst += 1
        #     else:
        #         numSecond += 1
        #     index += 1
        # return 1 + self.balancedStringSplit(s[index:])

        num, res = 0, 0
        for c in s:
            num += 1 if c == 'L' else -1
            if num == 0: res += 1
        return res


s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
