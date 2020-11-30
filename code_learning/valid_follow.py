class Solution:
    def isValid(self, s):
        stack = []
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack) != 0:
                    element = stack.pop(0)
                    if x != element:
                        return False
                    else:
                        continue
                else:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    print(solution.isValid("()[]{}"))
