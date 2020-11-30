class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums:
            slow = 0
            fast = 1
            while fast < len(nums):
                if nums[slow] != nums[fast]:
                    slow += 1
                    nums[slow] = nums[fast]

                fast += 1
            return slow+1
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates(list(map(int,input("input an array:").split(" ")))))
    print(solution.removeDuplicates([0, 1, 1, 2, 3, 3, 4]))
