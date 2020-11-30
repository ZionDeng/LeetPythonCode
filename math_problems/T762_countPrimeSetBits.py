# 给定两个整数 L 和 R ，找到闭区间 [L, R] 
# 范围内，计算置位位数为质数的整数个数。

# （注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 
# 10101 有 3 个计算置位。还有，1 不是质数。）

def is_prime(num:int) -> bool:
    if num == 1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        for i in range(L,R+1):
            x = bin(i).count("1")
            if is_prime(x):
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimeSetBits(10,15))
