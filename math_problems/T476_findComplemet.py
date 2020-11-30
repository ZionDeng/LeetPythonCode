# 数字的补位

class Solution:
    def findComplement(self, num: int) -> int:
        result = bin(num)[2:]
        temp = ''
        for i in result:
            if i == '1':
                temp += '0'
            else:
                temp += '1'
        return int(temp,2)


if __name__ == "__main__":
    s = Solution()
    print(s.findComplement(1))
