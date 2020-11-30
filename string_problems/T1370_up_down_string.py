class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        list = []
        for char in s:
            list.append(char)
        list.sort()
        flag=True
        while len(res) < len(s):
            resChar = list[0]
            res += resChar
            list.remove(resChar)

            if flag:
                for char in list:
                    if char > resChar:
                        resChar = char
                        list.remove(char)
                        res += char
            else:
                for char in list:
                    if char < resChar:
                        resChar = char
                        list.remove(char)
                        res += char

            list.reverse()
            flag = not flag

        return res


s = Solution()
print("o">"l")
print(s.sortString("leetcode"))
