class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        numStart = 0
        num=0
        result = ""
        for i, char in enumerate(S):
            if char == "(":
                num += 1
            else:
                num -= 1
            if num == 0:
                result+=S[numStart+1:i]
                numStart=i+1


        return result


s = Solution()
print(s.removeOuterParentheses("(()())(())"))
