# 给定一个整数数组 nums，
# 其中恰好有两个元素只出现一次，
# 其余所有元素均出现两次。 
# 找出只出现一次的那两个元素。

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        acc = 0
        for i in nums:
            acc ^=i
        n = len(bin(acc))-3
        a,b=0,0
        for i in nums:
            if i>>n&1:
                a^=i
            else:
                b^=i
        return b,a

s = Solution()
print(s.singleNumber([1,3,1,3,2,5]))
