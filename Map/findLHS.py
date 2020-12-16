# https://leetcode-cn.com/problems/longest-harmonious-subsequence/submissions/
import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = collections.Counter(nums)
        for num in nums:
            if num + 1 in d:
                res = max(res, d[num] + d[num+1])
        return res

        ''' method 2 
        nums.sort()
        begin, res = 0,0 
        for end in range(len(nums)):
            while nums[end] - nums[begin] >1:
                begin +=1
            if nums[end] - nums[begin] == 1:
                res = max(res,end - begin +1)
        return res 
        '''


s = Solution()
print(s.findLHS([1,2,2,2,2,3,5,6]))
