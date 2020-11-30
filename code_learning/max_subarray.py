import sys


class Solution:
    def maxSubArrayOne(self, nums) -> int:

        """暴力破解"""
        n = len(nums)
        maxSum = -sys.maxsize

        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                maxSum = max(maxSum, sum)

        return maxSum

    def maxSubArrayTwo(self, nums) -> int:
        """优化前缀和"""
        # sum(j~i)=S(i)-S(j)

        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)

        return maxSum

    def maxSubArray3(self, nums) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    def helper(self, nums, l, r):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        sum = 0
        for i in reversed(range(l, mid)):
            sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, sum)
        sum = 0
        for i in range(mid + 1, r + 1):
            sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)

    def maxSubArray4(self, nums) -> int:
        """动态规划"""
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)

        return max_sum

if __name__ == '__main__':
    s = Solution()
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(s.maxSubArrayOne(array))
    # print(s.maxSubArrayTwo(array))
    print(s.maxSubArray4(array))
