# 配对交换。编写程序，
# 交换某个整数的奇数位和偶数位，
# 尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

class Solution:
    def exchangeBits(self, num: int) -> int:
        i,j = 0,1
        num = list(bin(num)[2:])
        if len(num)%2==1:
            num = ['0']+num
        while i<len(num) and j<len(num):
            num[i],num[j] = num[j],num[i]
            i += 2
            j += 2
        print(num)
        return int(''.join(num),2)  # 数组→字符串→整形

if __name__ == "__main__":
    s= Solution()
    print(s.exchangeBits(2))
