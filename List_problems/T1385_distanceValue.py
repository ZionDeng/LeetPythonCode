from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for item1 in arr1:
            is_value = True
            for item2 in arr2:
                if abs(item1 - item2) <= d:
                    is_value = False
            if is_value:
                result += 1
        return result
        # return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)
    


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDistanceValue([4, 2, 3],
                                 [-4, -3, 6, 10, 20, 30],
                                 2))
