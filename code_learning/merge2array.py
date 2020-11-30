


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 整体思路相似，只不过没有使用 current 指针记录当前填补位置
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        """
        由于没有使用 current，第一步比较结束后有两种情况:
            1. 指针 m>0，n=0，此时不需要做任何处理
            2. 指针 n>0，m=0，此时需要将 nums2 指针左侧元素全部拷贝到 nums1 的前 n 位
        """
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    s = Solution()
    array1 = [1, 2, 3, 0, 0, 0]
    array2 = [2, 5, 6]

    print(s.merge(array1, 3, array2, 3))

    print(array1)
