#
# Given an array of integers arr, 
# write a function that returns true
# if and only if the number of occurrences of each value in the array is unique.
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        times = []
        for i in set(arr):
            time = arr.count(i)
            if time not in times:
                times.append(time)
            else:
                return False
        return True



if __name__ == '__main__':
    s = Solution()
    print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))