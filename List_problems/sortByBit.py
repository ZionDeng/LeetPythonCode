# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。

# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。

# 请你返回排序后的数组。


class Solution:
    def sortByBits(self, arr):
        # times = [bin(i).count('1') for i in arr]
        # return [i[1] for i in sorted(zip(times,arr))]

        return sorted(arr,key=lambda x:(bin(x).count('1'),x))


s = Solution()
print(s.sortByBits([i for i in range(9)]))
