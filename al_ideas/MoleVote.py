# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。


# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution:
    def majorityElement(self, nums) -> int:
        # nums.sort()
        # return nums[len(nums)//2]

        # mole vote
        count = 0
        card = None
        for num in nums:
            if count == 0:
                card = num
            count += 1 if card == num else -1
        return card


s = Solution()
print(s.majorityElement([1,2,2,2,3]))
