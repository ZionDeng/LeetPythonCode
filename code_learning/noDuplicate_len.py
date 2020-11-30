class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    # print(solution.removeDuplicates(list(map(int,input("input an array:").split(" ")))))
    print(solution.removeDuplicates([0, 1, 1, 2, 3, 3, 4]))
